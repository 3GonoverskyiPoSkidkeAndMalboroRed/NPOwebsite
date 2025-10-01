#!/usr/bin/env python3
"""
Скрипт для миграции данных методик в базу данных
"""

import os
import sys
from sqlalchemy import create_engine, text
from database import DATABASE_URL

def run_migration():
    """Запуск миграции данных методик"""
    try:
        # Создаем подключение к БД
        engine = create_engine(DATABASE_URL)
        
        # Читаем SQL файл
        with open('insert_methods.sql', 'r', encoding='utf-8') as f:
            sql_content = f.read()
        
        # Выполняем SQL
        with engine.connect() as conn:
            # Разделяем SQL на отдельные запросы
            statements = [stmt.strip() for stmt in sql_content.split(';') if stmt.strip()]
            
            for statement in statements:
                if statement:
                    try:
                        conn.execute(text(statement))
                        print(f"✓ Выполнен запрос: {statement[:50]}...")
                    except Exception as e:
                        print(f"✗ Ошибка выполнения запроса: {statement[:50]}...")
                        print(f"  Ошибка: {e}")
                        # Продолжаем выполнение других запросов
                        continue
            
            conn.commit()
            print("✓ Миграция завершена успешно!")
            
    except Exception as e:
        print(f"✗ Ошибка миграции: {e}")
        sys.exit(1)

if __name__ == "__main__":
    print("Запуск миграции данных методик...")
    run_migration()
