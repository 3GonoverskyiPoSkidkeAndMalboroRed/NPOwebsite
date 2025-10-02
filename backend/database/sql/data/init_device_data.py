#!/usr/bin/env python3
"""
Скрипт для инициализации типов приборов и их диапазонов серийных номеров
"""

import os
import sys
from sqlalchemy import create_engine, text
from database import DeviceType, SerialRange, get_db

def init_device_types():
    """Инициализация типов приборов и их диапазонов"""
    
    # Настройка подключения к БД
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/npo_db")
    engine = create_engine(DATABASE_URL)
    
    # Создание таблиц
    from database import Base
    Base.metadata.create_all(bind=engine)
    
    # Получение сессии
    db = next(get_db())
    
    try:
        # Данные о типах приборов и их диапазонах
        device_data = {
            'SE02': {
                'description': 'Спектрометр SE02',
                'ranges': [(60000, 60999)]
            },
            'SE03': {
                'description': 'Спектрометр SE03 (Спектр-Квант и SXRAY)',
                'ranges': [(61000, 61999), (62000, 62999)]
            },
            'G': {
                'description': 'Газоанализатор G',
                'ranges': [(6000, 6999)]
            },
            'SW-D3': {
                'description': 'Анализатор SW-D3',
                'ranges': [(7100, 7999)]
            },
            'MSW': {
                'description': 'Анализатор MSW',
                'ranges': [(8037, 8037), (8040, 8040), (12000, 12999)]
            },
            'CLSW': {
                'description': 'Анализатор CLSW',
                'ranges': [(8000, 8036), (8041, 8999)]
            },
            'META': {
                'description': 'Анализатор META',
                'ranges': [(11200, 11999)]
            },
            'GVM': {
                'description': 'Анализатор GVM',
                'ranges': [(9000, 9300)]
            },
            'S': {
                'description': 'Анализатор S',
                'ranges': [(5001, 5999), (9990, 9999), (50000, 59999), (10000, 10999)]
            }
        }
        
        # Создание типов приборов
        for device_name, device_info in device_data.items():
            # Проверяем, существует ли уже такой тип прибора
            existing_device = db.query(DeviceType).filter(DeviceType.name == device_name).first()
            
            if not existing_device:
                device_type = DeviceType(
                    name=device_name,
                    description=device_info['description']
                )
                db.add(device_type)
                db.flush()  # Получаем ID
                print(f"Создан тип прибора: {device_name}")
            else:
                device_type = existing_device
                print(f"Тип прибора уже существует: {device_name}")
            
            # Создание диапазонов серийных номеров
            for min_val, max_val in device_info['ranges']:
                # Проверяем, существует ли уже такой диапазон
                existing_range = db.query(SerialRange).filter(
                    SerialRange.device_type_id == device_type.id,
                    SerialRange.min_value == min_val,
                    SerialRange.max_value == max_val
                ).first()
                
                if not existing_range:
                    serial_range = SerialRange(
                        device_type_id=device_type.id,
                        min_value=min_val,
                        max_value=max_val
                    )
                    db.add(serial_range)
                    print(f"  Добавлен диапазон: {min_val}-{max_val}")
                else:
                    print(f"  Диапазон уже существует: {min_val}-{max_val}")
        
        # Сохранение изменений
        db.commit()
        print("\nИнициализация завершена успешно!")
        
        # Вывод статистики
        device_count = db.query(DeviceType).count()
        range_count = db.query(SerialRange).count()
        print(f"Всего типов приборов: {device_count}")
        print(f"Всего диапазонов: {range_count}")
        
    except Exception as e:
        print(f"Ошибка при инициализации: {e}")
        db.rollback()
        sys.exit(1)
    finally:
        db.close()

if __name__ == "__main__":
    init_device_types()
