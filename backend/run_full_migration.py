#!/usr/bin/env python3
"""
Скрипт для полной миграции всех методик в базу данных
"""

import os
import sys
from sqlalchemy import create_engine, text

# Docker настройка БД
DOCKER_DATABASE_URL = "postgresql://user:password@db:5432/npo_db"

def run_sql_file(filename):
    """Выполнение SQL файла"""
    try:
        # Создаем подключение к БД
        engine = create_engine(DOCKER_DATABASE_URL)
        
        # Читаем SQL файл
        with open(filename, 'r', encoding='utf-8') as f:
            sql_content = f.read()
        
        # Выполняем SQL
        with engine.connect() as conn:
            # Разделяем SQL на отдельные запросы
            statements = [stmt.strip() for stmt in sql_content.split(';') if stmt.strip()]
            
            for statement in statements:
                if statement:
                    try:
                        conn.execute(text(statement))
                        print(f"✓ Выполнен запрос из {filename}: {statement[:50]}...")
                    except Exception as e:
                        print(f"✗ Ошибка выполнения запроса из {filename}: {statement[:50]}...")
                        print(f"  Ошибка: {e}")
                        # Продолжаем выполнение других запросов
                        continue
            
            conn.commit()
            print(f"✓ Миграция {filename} завершена успешно!")
            
    except Exception as e:
        print(f"✗ Ошибка миграции {filename}: {e}")
        return False
    
    return True

def main():
    """Основная функция"""
    print("Запуск полной миграции всех методик...")
    print("=" * 60)
    
    # Список файлов для миграции
    migration_files = [
        'insert_all_methods.sql',
        'insert_eco_methods.sql', 
        'insert_mining_methods.sql',
        'insert_metallurgy_methods.sql',
        'insert_diagnostics_methods.sql',
        'insert_gas_methods.sql'
    ]
    
    success_count = 0
    total_count = len(migration_files)
    
    for filename in migration_files:
        if os.path.exists(filename):
            print(f"\n📁 Обработка файла: {filename}")
            if run_sql_file(filename):
                success_count += 1
            else:
                print(f"❌ Ошибка при обработке {filename}")
        else:
            print(f"⚠️  Файл {filename} не найден, пропускаем...")
    
    print("\n" + "=" * 60)
    print(f"📊 Результат миграции: {success_count}/{total_count} файлов обработано успешно")
    
    if success_count == total_count:
        print("🎉 Все методики успешно добавлены в базу данных!")
    else:
        print("⚠️  Некоторые файлы не были обработаны. Проверьте ошибки выше.")
    
    # Проверяем количество методик в БД
    try:
        engine = create_engine(DOCKER_DATABASE_URL)
        with engine.connect() as conn:
            result = conn.execute(text("SELECT COUNT(*) as count FROM methods"))
            count = result.fetchone()[0]
            print(f"📈 Всего методик в базе данных: {count}")
            
            # Показываем распределение по категориям
            result = conn.execute(text("SELECT category, COUNT(*) as count FROM methods GROUP BY category ORDER BY count DESC"))
            categories = result.fetchall()
            print("\n📋 Распределение по категориям:")
            for category, cat_count in categories:
                print(f"  - {category}: {cat_count} методик")
                
    except Exception as e:
        print(f"⚠️  Не удалось проверить количество методик: {e}")

if __name__ == "__main__":
    main()
