from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
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

# Создание таблиц
Base.metadata.create_all(bind=engine)

# Настройки для файлов
UPLOAD_DIR = "uploads/software_updates"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Настройки для JWT
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Зависимость для получения сессии БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
