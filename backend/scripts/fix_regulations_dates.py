#!/usr/bin/env python3
"""
Скрипт для исправления дат в существующих записях нормативных документов
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import SessionLocal, Regulation
from datetime import datetime

def fix_regulations_dates():
    """Исправление дат в существующих записях"""
    db = SessionLocal()
    try:
        # Получаем все записи с пустыми датами
        regulations = db.query(Regulation).filter(
            Regulation.created_at.is_(None) | Regulation.updated_at.is_(None)
        ).all()
        
        if not regulations:
            print("Все записи уже имеют корректные даты.")
            return
        
        print(f"Найдено {len(regulations)} записей с пустыми датами.")
        
        # Устанавливаем даты для каждой записи
        current_time = datetime.utcnow()
        for regulation in regulations:
            if regulation.created_at is None:
                regulation.created_at = current_time
            if regulation.updated_at is None:
                regulation.updated_at = current_time
        
        db.commit()
        print(f"Успешно обновлено {len(regulations)} записей.")
        
    except Exception as e:
        print(f"Ошибка при обновлении дат: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    print("Исправление дат в записях нормативных документов...")
    fix_regulations_dates()
