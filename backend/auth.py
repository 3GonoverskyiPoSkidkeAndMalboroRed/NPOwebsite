from fastapi import APIRouter, HTTPException, Depends, UploadFile, File, Form
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import datetime, timedelta
import os
import bcrypt
import jwt
from typing import Optional

from database import get_db, User, SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, validate_serial_number, get_device_type_by_serial

# Создаем роутер для аутентификации
auth_router = APIRouter(prefix="/auth", tags=["Аутентификация"])

# Pydantic модели для пользователей
class UserCreate(BaseModel):
    serial_number: str  # Серийный номер прибора
    inn: str  # ИНН
    kpp: str  # КПП
    password: str
    full_name: str  # ФИО
    position: str  # Должность
    organization: str  # Организация
    phone: str  # Телефон
    email: str  # Email

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    position: Optional[str] = None
    organization: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None

class DeviceTypeResponse(BaseModel):
    id: int
    name: str
    description: str
    
    class Config:
        from_attributes = True

class UserResponse(BaseModel):
    id: int
    serial_number: str
    device_type: Optional[DeviceTypeResponse] = None
    inn: str
    kpp: str
    full_name: str
    position: str
    organization: str
    phone: str
    email: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    serial_number: str  # Серийный номер прибора
    inn: str  # ИНН
    kpp: str  # КПП
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

# Функции для работы с паролями и токенами
def hash_password(password: str) -> str:
    """Хеширует пароль с использованием bcrypt"""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Проверяет пароль с использованием bcrypt"""
    try:
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
    except (ValueError, TypeError):
        return False

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Функции аутентификации
security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Неверный токен")
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Неверный токен")
    
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=401, detail="Пользователь не найден")
    return user

# Эндпоинты для аутентификации
@auth_router.post("/register", response_model=UserResponse)
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    """Регистрация нового пользователя"""
    # Валидация серийного номера с использованием БД
    if not validate_serial_number(user.serial_number, db):
        raise HTTPException(status_code=400, detail="Неверный серийный номер прибора")
    
    # Получаем тип прибора по серийному номеру
    device_type = get_device_type_by_serial(user.serial_number, db)
    
    # Проверяем, существует ли пользователь с таким серийным номером
    existing_user = db.query(User).filter(User.serial_number == user.serial_number).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Пользователь с таким серийным номером уже существует")
    
    # Проверяем, существует ли пользователь с такой комбинацией ИНН/КПП
    existing_org_user = db.query(User).filter(
        User.inn == user.inn, 
        User.kpp == user.kpp
    ).first()
    if existing_org_user:
        raise HTTPException(status_code=400, detail="Пользователь с такой комбинацией ИНН/КПП уже существует")
    
    # Создаем нового пользователя
    hashed_password = hash_password(user.password)
    db_user = User(
        serial_number=user.serial_number,
        device_type_id=device_type.id if device_type else None,
        inn=user.inn,
        kpp=user.kpp,
        password_hash=hashed_password,
        full_name=user.full_name,
        position=user.position,
        organization=user.organization,
        phone=user.phone,
        email=user.email
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user

@auth_router.post("/login", response_model=Token)
async def login_user(user_credentials: UserLogin, db: Session = Depends(get_db)):
    """Вход в систему"""
    # Ищем пользователя по серийному номеру, ИНН и КПП
    user = db.query(User).filter(
        User.serial_number == user_credentials.serial_number,
        User.inn == user_credentials.inn,
        User.kpp == user_credentials.kpp
    ).first()
    
    if not user or not verify_password(user_credentials.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Неверные данные для входа")
    
    access_token = create_access_token(data={"sub": str(user.id)})
    return {"access_token": access_token, "token_type": "bearer"}

@auth_router.get("/me", response_model=UserResponse)
async def get_current_user_info(current_user: User = Depends(get_current_user)):
    """Получение информации о текущем пользователе"""
    return current_user

@auth_router.put("/me", response_model=UserResponse)
async def update_current_user(
    user_update: UserUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Обновление информации о текущем пользователе"""
    # Обновляем только переданные поля
    update_data = user_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(current_user, field, value)
    
    current_user.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(current_user)
    
    return current_user

@auth_router.delete("/me")
async def delete_current_user(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Удаление текущего пользователя"""
    db.delete(current_user)
    db.commit()
    return {"message": "Пользователь успешно удален"}
