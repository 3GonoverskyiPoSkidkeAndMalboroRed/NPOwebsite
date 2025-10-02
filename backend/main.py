from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

# Импортируем из database.py
from database import get_db, Analysis, User, SoftwareUpdate, UPLOAD_DIR, SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

# Импортируем роутеры
from endpoints.auth import auth_router
from endpoints.files import files_router
from endpoints.methods import methods_router
from endpoints.regulations import regulations_router

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


# Подключаем роутеры
app.include_router(auth_router)
app.include_router(files_router)
app.include_router(methods_router)
app.include_router(regulations_router)

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


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
