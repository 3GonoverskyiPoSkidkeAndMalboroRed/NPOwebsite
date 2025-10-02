# Инструкции по миграции системы серийных номеров

## Шаги для применения изменений

### 1. Остановка сервисов
```bash
docker-compose down
```

### 2. Применение миграции базы данных
```bash
# Выполните SQL миграцию
psql -h localhost -U user -d npo_db -f backend/init_device_types.sql
```

### 3. Инициализация данных
```bash
# Запустите скрипт инициализации
python backend/init_device_data.py
```

### 4. Тестирование системы
```bash
# Запустите тесты
python backend/test_device_types.py
```

### 5. Запуск сервисов
```bash
docker-compose up -d
```

## Проверка миграции

### Проверка таблиц
```sql
-- Проверка типов приборов
SELECT * FROM device_types ORDER BY name;

-- Проверка диапазонов
SELECT dt.name, sr.min_value, sr.max_value 
FROM device_types dt 
JOIN serial_ranges sr ON dt.id = sr.device_type_id 
ORDER BY dt.name, sr.min_value;

-- Проверка пользователей с типами приборов
SELECT u.serial_number, dt.name as device_type, u.full_name
FROM users u
LEFT JOIN device_types dt ON u.device_type_id = dt.id;
```

### Проверка API
```bash
# Тест валидации серийного номера
curl -X POST "http://localhost:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "serial_number": "SE0260001",
    "inn": "1234567890",
    "kpp": "123456789",
    "password": "testpassword",
    "full_name": "Тест Тестович",
    "position": "Инженер",
    "organization": "Тестовая организация",
    "phone": "+7-999-123-45-67",
    "email": "test@example.com"
  }'
```

## Откат изменений (если необходимо)

### Удаление новых таблиц
```sql
-- Удаление диапазонов
DROP TABLE IF EXISTS serial_ranges;

-- Удаление типов приборов
DROP TABLE IF EXISTS device_types;

-- Удаление колонки из users
ALTER TABLE users DROP COLUMN IF EXISTS device_type_id;
```

## Структура файлов

```
backend/
├── database.py                 # Обновленные модели и функции
├── auth.py                     # Обновленная аутентификация
├── init_device_types.sql       # SQL миграция
├── init_device_data.py         # Python скрипт инициализации
├── test_device_types.py        # Тесты системы
├── README_DEVICE_TYPES.md      # Документация
└── MIGRATION_INSTRUCTIONS.md   # Данный файл
```

## Поддерживаемые серийные номера

| Префикс | Диапазоны | Примеры |
|---------|-----------|---------|
| SE02 | 60000-60999 | SE0260001, SE0260999 |
| SE03 | 61000-61999, 62000-62999 | SE0361001, SE0362001 |
| G | 6000-6999 | G6001, G6999 |
| SW-D3 | 7100-7999 | SW-D37101, SW-D37999 |
| MSW | 8037, 8040, 12000-12999 | MSW8037, MSW12001 |
| CLSW | 8000-8036, 8041-8999 | CLSW8001, CLSW8041 |
| META | 11200-11999 | META11201, META11999 |
| GVM | 9000-9300 | GVM9001, GVM9300 |
| S | 5001-5999, 9990-9999, 50000-59999, 10000-10999 | S5001, S9990, S50001, S10001 |

## Устранение неполадок

### Ошибка подключения к БД
```bash
# Проверьте настройки подключения
echo $DATABASE_URL
```

### Ошибки валидации
```bash
# Запустите тесты для диагностики
python backend/test_device_types.py
```

### Проблемы с миграцией
```bash
# Проверьте логи PostgreSQL
docker-compose logs db
```
