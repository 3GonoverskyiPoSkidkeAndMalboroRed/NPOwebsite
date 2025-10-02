from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

from database import get_db, Regulation

# Pydantic модели
class RegulationBase(BaseModel):
    code: str
    title: str
    company: str
    category: str
    year: str
    description: Optional[str] = None
    file_path: Optional[str] = None

class RegulationCreate(RegulationBase):
    pass

class RegulationUpdate(BaseModel):
    code: Optional[str] = None
    title: Optional[str] = None
    company: Optional[str] = None
    category: Optional[str] = None
    year: Optional[str] = None
    description: Optional[str] = None
    file_path: Optional[str] = None
    is_active: Optional[int] = None

class RegulationResponse(RegulationBase):
    id: int
    is_active: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

# Создание роутера
regulations_router = APIRouter(prefix="/regulations", tags=["regulations"])

@regulations_router.get("/", response_model=List[RegulationResponse])
async def get_regulations(
    category: Optional[str] = Query(None, description="Фильтр по категории"),
    search: Optional[str] = Query(None, description="Поиск по коду, названию или категории"),
    is_active: Optional[int] = Query(1, description="Фильтр по активности (1 - активные, 0 - неактивные)"),
    db: Session = Depends(get_db)
):
    """Получение списка нормативных документов с фильтрацией"""
    query = db.query(Regulation)
    
    # Фильтр по активности
    if is_active is not None:
        query = query.filter(Regulation.is_active == is_active)
    
    # Фильтр по категории
    if category and category != "all":
        query = query.filter(Regulation.category == category)
    
    # Поиск по тексту
    if search:
        search_term = f"%{search.lower()}%"
        query = query.filter(
            db.or_(
                Regulation.code.ilike(search_term),
                Regulation.title.ilike(search_term),
                Regulation.category.ilike(search_term)
            )
        )
    
    regulations = query.order_by(Regulation.year.desc(), Regulation.code).all()
    return regulations

@regulations_router.get("/{regulation_id}", response_model=RegulationResponse)
async def get_regulation(regulation_id: int, db: Session = Depends(get_db)):
    """Получение нормативного документа по ID"""
    regulation = db.query(Regulation).filter(Regulation.id == regulation_id).first()
    if not regulation:
        raise HTTPException(status_code=404, detail="Нормативный документ не найден")
    return regulation

@regulations_router.post("/", response_model=RegulationResponse)
async def create_regulation(regulation: RegulationCreate, db: Session = Depends(get_db)):
    """Создание нового нормативного документа"""
    db_regulation = Regulation(**regulation.dict())
    db.add(db_regulation)
    db.commit()
    db.refresh(db_regulation)
    return db_regulation

@regulations_router.put("/{regulation_id}", response_model=RegulationResponse)
async def update_regulation(
    regulation_id: int, 
    regulation_update: RegulationUpdate, 
    db: Session = Depends(get_db)
):
    """Обновление нормативного документа"""
    db_regulation = db.query(Regulation).filter(Regulation.id == regulation_id).first()
    if not db_regulation:
        raise HTTPException(status_code=404, detail="Нормативный документ не найден")
    
    update_data = regulation_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_regulation, field, value)
    
    db_regulation.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(db_regulation)
    return db_regulation

@regulations_router.delete("/{regulation_id}")
async def delete_regulation(regulation_id: int, db: Session = Depends(get_db)):
    """Мягкое удаление нормативного документа"""
    db_regulation = db.query(Regulation).filter(Regulation.id == regulation_id).first()
    if not db_regulation:
        raise HTTPException(status_code=404, detail="Нормативный документ не найден")
    
    db_regulation.is_active = 0
    db_regulation.updated_at = datetime.utcnow()
    db.commit()
    return {"message": "Нормативный документ успешно удален"}

@regulations_router.get("/categories/list", response_model=List[str])
async def get_categories(db: Session = Depends(get_db)):
    """Получение списка всех категорий нормативных документов"""
    categories = db.query(Regulation.category).filter(Regulation.is_active == 1).distinct().all()
    return [cat[0] for cat in categories]

@regulations_router.get("/stats/summary")
async def get_regulations_stats(db: Session = Depends(get_db)):
    """Получение статистики по нормативным документам"""
    total = db.query(Regulation).filter(Regulation.is_active == 1).count()
    categories_count = db.query(Regulation.category).filter(Regulation.is_active == 1).distinct().count()
    modern_count = db.query(Regulation).filter(
        Regulation.is_active == 1,
        Regulation.year >= '2020'
    ).count()
    
    return {
        "total": total,
        "categories": categories_count,
        "modern": modern_count
    }
