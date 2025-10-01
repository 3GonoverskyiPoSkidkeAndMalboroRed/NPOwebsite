from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import json

from database import get_db, Method

# Создаем роутер
methods_router = APIRouter(prefix="/methods", tags=["methods"])

# Pydantic модели
class MethodDocumentation(BaseModel):
    title: str
    description: str
    link: Optional[str] = None

class MethodEquipment(BaseModel):
    name: str
    description: str
    specifications: Optional[str] = None

class MethodCreate(BaseModel):
    title: str
    standards_description: Optional[str] = None
    method_description: Optional[str] = None
    description_content: Optional[List[str]] = None
    limitations: Optional[str] = None
    procedure: Optional[List[str]] = None
    documentation: Optional[List[MethodDocumentation]] = None
    equipment: Optional[List[MethodEquipment]] = None
    category: str
    is_active: int = 1

class MethodResponse(BaseModel):
    id: int
    title: str
    standards_description: Optional[str]
    method_description: Optional[str]
    description_content: Optional[List[str]]
    limitations: Optional[str]
    procedure: Optional[List[str]]
    documentation: Optional[List[MethodDocumentation]]
    equipment: Optional[List[MethodEquipment]]
    category: str
    is_active: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class MethodUpdate(BaseModel):
    title: Optional[str] = None
    standards_description: Optional[str] = None
    method_description: Optional[str] = None
    description_content: Optional[List[str]] = None
    limitations: Optional[str] = None
    procedure: Optional[List[str]] = None
    documentation: Optional[List[MethodDocumentation]] = None
    equipment: Optional[List[MethodEquipment]] = None
    category: Optional[str] = None
    is_active: Optional[int] = None

# Endpoints
@methods_router.get("/", response_model=List[MethodResponse])
async def get_methods(
    category: Optional[str] = None,
    is_active: Optional[int] = None,
    db: Session = Depends(get_db)
):
    """Получить список методик с возможностью фильтрации"""
    query = db.query(Method)
    
    if category:
        query = query.filter(Method.category == category)
    
    if is_active is not None:
        query = query.filter(Method.is_active == is_active)
    
    methods = query.all()
    return methods

@methods_router.get("/{method_id}", response_model=MethodResponse)
async def get_method(method_id: int, db: Session = Depends(get_db)):
    """Получить методику по ID"""
    method = db.query(Method).filter(Method.id == method_id).first()
    if not method:
        raise HTTPException(status_code=404, detail="Методика не найдена")
    return method

@methods_router.post("/", response_model=MethodResponse)
async def create_method(method: MethodCreate, db: Session = Depends(get_db)):
    """Создать новую методику"""
    # Преобразуем Pydantic модели в JSON для хранения в БД
    method_data = method.dict()
    
    # Обрабатываем JSON поля
    if method_data.get('documentation'):
        method_data['documentation'] = [doc.dict() for doc in method_data['documentation']]
    if method_data.get('equipment'):
        method_data['equipment'] = [eq.dict() for eq in method_data['equipment']]
    
    db_method = Method(**method_data)
    db.add(db_method)
    db.commit()
    db.refresh(db_method)
    return db_method

@methods_router.put("/{method_id}", response_model=MethodResponse)
async def update_method(
    method_id: int, 
    method_update: MethodUpdate, 
    db: Session = Depends(get_db)
):
    """Обновить методику"""
    method = db.query(Method).filter(Method.id == method_id).first()
    if not method:
        raise HTTPException(status_code=404, detail="Методика не найдена")
    
    # Обновляем только переданные поля
    update_data = method_update.dict(exclude_unset=True)
    
    # Обрабатываем JSON поля
    if 'documentation' in update_data and update_data['documentation']:
        update_data['documentation'] = [doc.dict() if hasattr(doc, 'dict') else doc for doc in update_data['documentation']]
    if 'equipment' in update_data and update_data['equipment']:
        update_data['equipment'] = [eq.dict() if hasattr(eq, 'dict') else eq for eq in update_data['equipment']]
    
    for field, value in update_data.items():
        setattr(method, field, value)
    
    method.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(method)
    return method

@methods_router.delete("/{method_id}")
async def delete_method(method_id: int, db: Session = Depends(get_db)):
    """Удалить методику (мягкое удаление - устанавливаем is_active = 0)"""
    method = db.query(Method).filter(Method.id == method_id).first()
    if not method:
        raise HTTPException(status_code=404, detail="Методика не найдена")
    
    method.is_active = 0
    method.updated_at = datetime.utcnow()
    db.commit()
    return {"message": "Методика успешно деактивирована"}

@methods_router.get("/categories/list")
async def get_categories(db: Session = Depends(get_db)):
    """Получить список всех категорий методик"""
    categories = db.query(Method.category).distinct().all()
    return [cat[0] for cat in categories if cat[0]]
