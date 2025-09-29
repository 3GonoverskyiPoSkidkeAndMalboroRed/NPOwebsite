from fastapi import FastAPI, HTTPException, Depends, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel, EmailStr
from datetime import datetime, timedelta
import os
import bcrypt
import jwt
import aiofiles
import shutil
from typing import List, Optional

# Настройка базы данных
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/npo_db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Модель базы данных
class Analysis(Base):
    __tablename__ = "analyses"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    method = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    organization = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    position = Column(String)
    phone = Column(String)
    email = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class SoftwareUpdate(Base):
    __tablename__ = "software_updates"
    
    id = Column(Integer, primary_key=True, index=True)
    version = Column(String, nullable=False)
    description = Column(Text)
    file_path = Column(String, nullable=False)
    file_size = Column(Float)
    file_name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    uploaded_by = Column(Integer, nullable=False)  # ID пользователя, загрузившего файл

# Pydantic модели
class AnalysisCreate(BaseModel):
    title: str
    description: str
    method: str

class AnalysisResponse(BaseModel):
    id: int
    title: str
    description: str
    method: str
    created_at: datetime
    
    class Config:
        from_attributes = True

# Pydantic модели для пользователей
class UserCreate(BaseModel):
    login: str
    password: str
    organization: str
    full_name: str
    position: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None

class UserUpdate(BaseModel):
    organization: Optional[str] = None
    full_name: Optional[str] = None
    position: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None

class UserResponse(BaseModel):
    id: int
    login: str
    organization: str
    full_name: str
    position: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    login: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

# Pydantic модели для файлов обновления ПО
class SoftwareUpdateResponse(BaseModel):
    id: int
    version: str
    description: Optional[str] = None
    file_name: str
    file_size: Optional[float] = None
    created_at: datetime
    uploaded_by: int
    
    class Config:
        from_attributes = True

class SoftwareUpdateCreate(BaseModel):
    version: str
    description: Optional[str] = None

# Создание таблиц
Base.metadata.create_all(bind=engine)

# Настройки для файлов
UPLOAD_DIR = "uploads/software_updates"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Настройки для JWT
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

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

# Инициализация FastAPI
app = FastAPI(
    title="NPO API",
    description="API для системы аналитических приборов",
    version="1.0.0"
)

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000", 
        "http://frontend:80", 
        "http://localhost:8081",
        "http://192.168.81.74:3000",
        "http://192.168.81.74:8081"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Зависимость для получения сессии БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Функции аутентификации
security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security), db: SessionLocal = Depends(get_db)):
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

@app.get("/")
async def root():
    return {"message": "NPO API работает!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.utcnow()}

@app.get("/analyses", response_model=List[AnalysisResponse])
async def get_analyses():
    db = SessionLocal()
    try:
        analyses = db.query(Analysis).all()
        return analyses
    finally:
        db.close()

@app.post("/analyses", response_model=AnalysisResponse)
async def create_analysis(analysis: AnalysisCreate):
    db = SessionLocal()
    try:
        db_analysis = Analysis(**analysis.dict())
        db.add(db_analysis)
        db.commit()
        db.refresh(db_analysis)
        return db_analysis
    finally:
        db.close()

@app.get("/analyses/{analysis_id}", response_model=AnalysisResponse)
async def get_analysis(analysis_id: int):
    db = SessionLocal()
    try:
        analysis = db.query(Analysis).filter(Analysis.id == analysis_id).first()
        if not analysis:
            raise HTTPException(status_code=404, detail="Анализ не найден")
        return analysis
    finally:
        db.close()

# Эндпоинты для личного кабинета
@app.post("/auth/register", response_model=UserResponse)
async def register_user(user: UserCreate, db: SessionLocal = Depends(get_db)):
    # Проверяем, существует ли пользователь с таким логином
    existing_user = db.query(User).filter(User.login == user.login).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Пользователь с таким логином уже существует")
    
    # Создаем нового пользователя
    hashed_password = hash_password(user.password)
    db_user = User(
        login=user.login,
        password_hash=hashed_password,
        organization=user.organization,
        full_name=user.full_name,
        position=user.position,
        phone=user.phone,
        email=user.email
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user

@app.post("/auth/login", response_model=Token)
async def login_user(user_credentials: UserLogin, db: SessionLocal = Depends(get_db)):
    user = db.query(User).filter(User.login == user_credentials.login).first()
    if not user or not verify_password(user_credentials.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Неверный логин или пароль")
    
    access_token = create_access_token(data={"sub": str(user.id)})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/auth/me", response_model=UserResponse)
async def get_current_user_info(current_user: User = Depends(get_current_user)):
    return current_user

@app.put("/auth/me", response_model=UserResponse)
async def update_current_user(
    user_update: UserUpdate,
    current_user: User = Depends(get_current_user),
    db: SessionLocal = Depends(get_db)
):
    # Обновляем только переданные поля
    update_data = user_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(current_user, field, value)
    
    current_user.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(current_user)
    
    return current_user

@app.delete("/auth/me")
async def delete_current_user(
    current_user: User = Depends(get_current_user),
    db: SessionLocal = Depends(get_db)
):
    db.delete(current_user)
    db.commit()
    return {"message": "Пользователь успешно удален"}

# Эндпоинты для файлов обновления ПО
@app.post("/software-updates/upload", response_model=SoftwareUpdateResponse)
async def upload_software_update(
    file: UploadFile = File(...),
    version: str = Form(...),
    description: Optional[str] = Form(None),
    current_user: User = Depends(get_current_user),
    db: SessionLocal = Depends(get_db)
):
    """Загрузка файла обновления ПО"""
    
    # Проверяем, что файл не пустой
    if not file.filename:
        raise HTTPException(status_code=400, detail="Файл не выбран")
    
    # Проверяем расширение файла (можно добавить дополнительные проверки)
    allowed_extensions = ['.zip', '.exe', '.msi', '.deb', '.rpm', '.dmg', '.pkg']
    file_extension = os.path.splitext(file.filename)[1].lower()
    if file_extension not in allowed_extensions:
        raise HTTPException(status_code=400, detail=f"Неподдерживаемый тип файла. Разрешены: {', '.join(allowed_extensions)}")
    
    # Создаем уникальное имя файла
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    safe_filename = f"{version}_{timestamp}{file_extension}"
    file_path = os.path.join(UPLOAD_DIR, safe_filename)
    
    try:
        # Сохраняем файл
        async with aiofiles.open(file_path, 'wb') as f:
            content = await file.read()
            await f.write(content)
        
        # Получаем размер файла
        file_size = len(content) / (1024 * 1024)  # Размер в МБ
        
        # Сохраняем информацию в базу данных
        db_update = SoftwareUpdate(
            version=version,
            description=description,
            file_path=file_path,
            file_size=file_size,
            file_name=file.filename,
            uploaded_by=current_user.id
        )
        
        db.add(db_update)
        db.commit()
        db.refresh(db_update)
        
        return db_update
        
    except Exception as e:
        # Удаляем файл в случае ошибки
        if os.path.exists(file_path):
            os.remove(file_path)
        raise HTTPException(status_code=500, detail=f"Ошибка при загрузке файла: {str(e)}")

@app.get("/software-updates", response_model=List[SoftwareUpdateResponse])
async def get_software_updates(
    db: SessionLocal = Depends(get_db)
):
    """Получение списка всех файлов обновления ПО"""
    
    updates = db.query(SoftwareUpdate).order_by(SoftwareUpdate.created_at.desc()).all()
    return updates

@app.get("/software-updates/{update_id}/download")
async def download_software_update(
    update_id: int,
    db: SessionLocal = Depends(get_db)
):
    """Скачивание файла обновления ПО"""
    
    update = db.query(SoftwareUpdate).filter(SoftwareUpdate.id == update_id).first()
    if not update:
        raise HTTPException(status_code=404, detail="Файл обновления не найден")
    
    if not os.path.exists(update.file_path):
        raise HTTPException(status_code=404, detail="Файл не найден на сервере")
    
    return FileResponse(
        path=update.file_path,
        filename=update.file_name,
        media_type='application/octet-stream'
    )

@app.delete("/software-updates/{update_id}")
async def delete_software_update(
    update_id: int,
    current_user: User = Depends(get_current_user),
    db: SessionLocal = Depends(get_db)
):
    """Удаление файла обновления ПО (только для администраторов или загрузившего файл)"""
    
    update = db.query(SoftwareUpdate).filter(SoftwareUpdate.id == update_id).first()
    if not update:
        raise HTTPException(status_code=404, detail="Файл обновления не найден")
    
    # Проверяем права доступа (только загрузивший файл может его удалить)
    if update.uploaded_by != current_user.id:
        raise HTTPException(status_code=403, detail="Недостаточно прав для удаления файла")
    
    try:
        # Удаляем файл с диска
        if os.path.exists(update.file_path):
            os.remove(update.file_path)
        
        # Удаляем запись из базы данных
        db.delete(update)
        db.commit()
        
        return {"message": "Файл обновления успешно удален"}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при удалении файла: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
