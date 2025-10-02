#!/usr/bin/env python3
"""
Универсальный скрипт для запуска миграции данных методик
Автоматически определяет способ запуска (локально или через Docker)
"""

import os
import sys
import subprocess
import socket

def check_docker_available():
    """Проверяет, доступен ли Docker и запущены ли контейнеры"""
    try:
        # Проверяем, запущен ли Docker
        result = subprocess.run(['docker', 'ps'], capture_output=True, text=True)
        if result.returncode != 0:
            return False
        
        # Проверяем, запущен ли наш контейнер с БД
        result = subprocess.run(['docker', 'ps', '--filter', 'name=npo_postgres'], capture_output=True, text=True)
        return 'npo_postgres' in result.stdout
    except FileNotFoundError:
        return False

def check_local_postgres():
    """Проверяет, доступна ли локальная PostgreSQL"""
    try:
        import psycopg2
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            database="npo_db",
            user="user",
            password="password"
        )
        conn.close()
        return True
    except:
        return False

def run_docker_migration():
    """Запуск миграции через Docker"""
    print("Запуск миграции через Docker...")
    
    # Проверяем, запущены ли контейнеры
    if not check_docker_available():
        print("Docker контейнеры не запущены!")
        print("Запустите: docker-compose up -d")
        return False
    
    # Запускаем миграцию в контейнере backend
    try:
        result = subprocess.run([
            'docker', 'exec', 'npo_backend', 
            'python', 'migrate_methods_docker.py'
        ], check=True, capture_output=True, text=True)
        
        print(result.stdout)
        if result.stderr:
            print("Предупреждения:", result.stderr)
        
        print("Миграция через Docker завершена успешно!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при запуске миграции через Docker: {e}")
        print("Вывод:", e.stdout)
        print("Ошибки:", e.stderr)
        return False

def run_local_migration():
    """Запуск локальной миграции"""
    print("Запуск локальной миграции...")
    
    if not check_local_postgres():
        print("Локальная PostgreSQL недоступна!")
        print("Убедитесь, что PostgreSQL запущен на localhost:5432")
        print("И создайте базу данных 'npo_db' с пользователем 'user'")
        return False
    
    try:
        # Импортируем и запускаем локальную миграцию
        from migrate_methods_local import run_migration
        run_migration()
        return True
    except Exception as e:
        print(f"Ошибка локальной миграции: {e}")
        return False

def main():
    """Основная функция"""
    print("Запуск миграции данных методик...")
    print("=" * 50)
    
    # Проверяем доступность Docker
    if check_docker_available():
        print("Обнаружен запущенный Docker с БД")
        if run_docker_migration():
            return
        else:
            print("\nМиграция через Docker не удалась, пробуем локально...")
    
    # Пробуем локальную миграцию
    if check_local_postgres():
        print("Обнаружена локальная PostgreSQL")
        if run_local_migration():
            return
        else:
            print("\nЛокальная миграция также не удалась")
    else:
        print("Локальная PostgreSQL недоступна")
    
    print("\n" + "=" * 50)
    print("Не удалось выполнить миграцию!")
    print("\nВозможные решения:")
    print("1. Запустите Docker: docker-compose up -d")
    print("2. Или настройте локальную PostgreSQL")
    print("3. Или выполните миграцию вручную через SQL")

if __name__ == "__main__":
    main()
