#!/usr/bin/env python3
"""
Скрипт для тестирования системы типов приборов и серийных номеров
"""

import os
import sys
from database import validate_serial_number, get_device_type_by_serial, get_db, DeviceType, SerialRange

def test_serial_validation():
    """Тестирование валидации серийных номеров"""
    print("=== Тестирование валидации серийных номеров ===")
    
    # Тестовые серийные номера
    test_serials = [
        # Валидные номера
        ("SE0260001", True, "SE02"),
        ("SE0361001", True, "SE03"),
        ("SE0362001", True, "SE03"),
        ("G6001", True, "G"),
        ("SW-D37101", True, "SW-D3"),
        ("MSW8037", True, "MSW"),
        ("MSW8040", True, "MSW"),
        ("MSW12001", True, "MSW"),
        ("CLSW8001", True, "CLSW"),
        ("CLSW8041", True, "CLSW"),
        ("META11201", True, "META"),
        ("GVM9001", True, "GVM"),
        ("S5001", True, "S"),
        ("S9990", True, "S"),
        ("S50001", True, "S"),
        ("S10001", True, "S"),
        
        # Невалидные номера
        ("INVALID123", False, None),
        ("SE0299999", False, None),  # Вне диапазона
        ("G9999", False, None),      # Вне диапазона
        ("UNKNOWN123", False, None),
    ]
    
    db = next(get_db())
    
    for serial, expected_valid, expected_type in test_serials:
        try:
            # Тест статической валидации
            static_valid = validate_serial_number(serial)
            
            # Тест валидации с БД
            db_valid = validate_serial_number(serial, db)
            
            # Тест получения типа прибора
            device_type = get_device_type_by_serial(serial, db)
            actual_type = device_type.name if device_type else None
            
            print(f"Серийный номер: {serial}")
            print(f"  Статическая валидация: {static_valid} (ожидается: {expected_valid})")
            print(f"  Валидация с БД: {db_valid} (ожидается: {expected_valid})")
            print(f"  Тип прибора: {actual_type} (ожидается: {expected_type})")
            
            # Проверка результатов
            if static_valid == expected_valid and db_valid == expected_valid:
                if expected_type is None or actual_type == expected_type:
                    print("  ✅ ПРОЙДЕН")
                else:
                    print("  ❌ ОШИБКА: Неверный тип прибора")
            else:
                print("  ❌ ОШИБКА: Неверная валидация")
            
            print()
            
        except Exception as e:
            print(f"  ❌ ОШИБКА: {e}")
            print()
    
    db.close()

def test_database_structure():
    """Тестирование структуры базы данных"""
    print("=== Тестирование структуры БД ===")
    
    db = next(get_db())
    
    try:
        # Проверка типов приборов
        device_types = db.query(DeviceType).all()
        print(f"Количество типов приборов: {len(device_types)}")
        
        for device_type in device_types:
            print(f"  {device_type.name}: {device_type.description}")
            ranges = db.query(SerialRange).filter(SerialRange.device_type_id == device_type.id).all()
            print(f"    Диапазоны: {[(r.min_value, r.max_value) for r in ranges]}")
        
        print()
        
        # Проверка диапазонов
        total_ranges = db.query(SerialRange).count()
        print(f"Общее количество диапазонов: {total_ranges}")
        
    except Exception as e:
        print(f"Ошибка при проверке БД: {e}")
    finally:
        db.close()

def main():
    """Основная функция"""
    print("Тестирование системы типов приборов и серийных номеров")
    print("=" * 60)
    
    try:
        test_database_structure()
        test_serial_validation()
        print("Тестирование завершено!")
        
    except Exception as e:
        print(f"Ошибка при тестировании: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
