from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
import os

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

class DeviceType(Base):
    __tablename__ = "device_types"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)  # Название типа прибора (SE02, SE03, G, etc.)
    description = Column(String)  # Описание типа прибора
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Связь с диапазонами серийных номеров
    serial_ranges = relationship("SerialRange", back_populates="device_type")

class SerialRange(Base):
    __tablename__ = "serial_ranges"
    
    id = Column(Integer, primary_key=True, index=True)
    device_type_id = Column(Integer, ForeignKey("device_types.id"), nullable=False)
    min_value = Column(Integer, nullable=False)  # Минимальное значение диапазона
    max_value = Column(Integer, nullable=False)  # Максимальное значение диапазона
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Связь с типом прибора
    device_type = relationship("DeviceType", back_populates="serial_ranges")

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    serial_number = Column(String, unique=True, index=True, nullable=False)  # Серийный номер прибора
    device_type_id = Column(Integer, ForeignKey("device_types.id"), nullable=True)  # Связь с типом прибора
    inn = Column(String, nullable=False)  # ИНН
    kpp = Column(String, nullable=False)  # КПП
    password_hash = Column(String, nullable=False)
    full_name = Column(String, nullable=False)  # ФИО
    position = Column(String, nullable=False)  # Должность
    organization = Column(String, nullable=False)  # Организация
    phone = Column(String, nullable=False)  # Телефон
    email = Column(String, nullable=False)  # Email
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Связь с типом прибора
    device_type = relationship("DeviceType")

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

# Создание таблиц
Base.metadata.create_all(bind=engine)

# Настройки для файлов
UPLOAD_DIR = "uploads/software_updates"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Настройки для JWT
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Функция валидации серийных номеров
def validate_serial_number(serial_number: str, db_session=None) -> bool:
    """Валидация серийного номера по диапазонам приборов из базы данных"""
    try:
        if not serial_number:
            return False
        
        # Если сессия БД не передана, используем статическую валидацию
        if db_session is None:
            return validate_serial_number_static(serial_number)
        
        # Получаем все типы приборов и их диапазоны из БД
        device_types = db_session.query(DeviceType).all()
        
        for device_type in device_types:
            if serial_number.startswith(device_type.name):
                # Извлекаем числовую часть
                number_part = serial_number[len(device_type.name):]
                if number_part.isdigit():
                    number = int(number_part)
                    # Проверяем все диапазоны для данного типа прибора
                    for range_obj in device_type.serial_ranges:
                        if range_obj.min_value <= number <= range_obj.max_value:
                            return True
        
        return False
    except (ValueError, TypeError):
        return False

def validate_serial_number_static(serial_number: str) -> bool:
    """Статическая валидация серийного номера (резервный метод)"""
    try:
        if not serial_number:
            return False
            
        # Определяем диапазоны для каждого типа прибора
        ranges = {
            'SE02': [(60000, 60999)],
            'SE03': [(61000, 61999), (62000, 62999)],  # Спектр-Квант и SXRAY
            'G': [(6000, 6999)],
            'SW-D3': [(7100, 7999)],
            'MSW': [(8037, 8037), (8040, 8040), (12000, 12999)],
            'CLSW': [(8000, 8036), (8041, 8999)],
            'META': [(11200, 11999)],
            'GVM': [(9000, 9300)],
            'S': [(5001, 5999), (9990, 9999), (50000, 59999), (10000, 10999)]
        }
        
        # Проверяем каждый префикс
        for prefix, number_ranges in ranges.items():
            if serial_number.startswith(prefix):
                # Извлекаем числовую часть
                number_part = serial_number[len(prefix):]
                if number_part.isdigit():
                    number = int(number_part)
                    for min_val, max_val in number_ranges:
                        if min_val <= number <= max_val:
                            return True
        
        return False
    except (ValueError, TypeError):
        return False

def get_device_type_by_serial(serial_number: str, db_session=None):
    """Получение типа прибора по серийному номеру"""
    try:
        if not serial_number:
            return None
        
        if db_session is None:
            return None
        
        # Получаем все типы приборов и их диапазоны из БД
        device_types = db_session.query(DeviceType).all()
        
        for device_type in device_types:
            if serial_number.startswith(device_type.name):
                # Извлекаем числовую часть
                number_part = serial_number[len(device_type.name):]
                if number_part.isdigit():
                    number = int(number_part)
                    # Проверяем все диапазоны для данного типа прибора
                    for range_obj in device_type.serial_ranges:
                        if range_obj.min_value <= number <= range_obj.max_value:
                            return device_type
        
        return None
    except (ValueError, TypeError):
        return None

# Зависимость для получения сессии БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
