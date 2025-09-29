from fastapi import APIRouter, HTTPException, Depends, UploadFile, File, Form
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import datetime
import os
import aiofiles
from typing import List, Optional

from database import get_db, SoftwareUpdate, UPLOAD_DIR
from auth import get_current_user, User

# Создаем роутер для работы с файлами
files_router = APIRouter(prefix="/software-updates", tags=["Файлы обновления ПО"])

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

# Эндпоинты для файлов обновления ПО
@files_router.post("/upload", response_model=SoftwareUpdateResponse)
async def upload_software_update(
    file: UploadFile = File(...),
    version: str = Form(...),
    description: Optional[str] = Form(None),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
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

@files_router.get("", response_model=List[SoftwareUpdateResponse])
async def get_software_updates(
    db: Session = Depends(get_db)
):
    """Получение списка всех файлов обновления ПО"""
    
    updates = db.query(SoftwareUpdate).order_by(SoftwareUpdate.created_at.desc()).all()
    return updates

@files_router.get("/{update_id}/download")
async def download_software_update(
    update_id: int,
    db: Session = Depends(get_db)
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

@files_router.delete("/{update_id}")
async def delete_software_update(
    update_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
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
