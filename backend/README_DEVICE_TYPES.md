# Миграция системы серийных номеров приборов

## Описание изменений

Добавлена новая система управления серийными номерами приборов с поддержкой различных типов устройств и их диапазонов.

## Новые таблицы

### device_types
- `id` - первичный ключ
- `name` - название типа прибора (SE02, SE03, G, etc.)
- `description` - описание типа прибора
- `created_at` - дата создания

### serial_ranges
- `id` - первичный ключ
- `device_type_id` - внешний ключ на device_types
- `min_value` - минимальное значение диапазона
- `max_value` - максимальное значение диапазона
- `created_at` - дата создания

## Изменения в таблице users

Добавлено поле `device_type_id` - связь с типом прибора.

## Поддерживаемые типы приборов и диапазоны

| Тип прибора | Диапазоны серийных номеров | Описание |
|-------------|---------------------------|----------|
| SE02 | 60000-60999 | Спектрометр SE02 |
| SE03 | 61000-61999, 62000-62999 | Спектрометр SE03 (Спектр-Квант и SXRAY) |
| G | 6000-6999 | Газоанализатор G |
| SW-D3 | 7100-7999 | Анализатор SW-D3 |
| MSW | 8037, 8040, 12000-12999 | Анализатор MSW |
| CLSW | 8000-8036, 8041-8999 | Анализатор CLSW |
| META | 11200-11999 | Анализатор META |
| GVM | 9000-9300 | Анализатор GVM |
| S | 5001-5999, 9990-9999, 50000-59999, 10000-10999 | Анализатор S |

## Инструкции по миграции

### 1. Запуск миграции SQL
```bash
# Подключитесь к базе данных и выполните:
psql -h localhost -U user -d npo_db -f backend/init_device_types.sql
```

### 2. Инициализация данных Python
```bash
# Запустите скрипт инициализации:
python backend/init_device_data.py
```

### 3. Проверка миграции
```sql
-- Проверьте созданные таблицы
SELECT * FROM device_types;
SELECT * FROM serial_ranges;

-- Проверьте связи
SELECT u.serial_number, dt.name as device_type
FROM users u
LEFT JOIN device_types dt ON u.device_type_id = dt.id;
```

## Новые функции

### validate_serial_number(serial_number, db_session=None)
Валидация серийного номера с использованием данных из БД или статической валидации.

### get_device_type_by_serial(serial_number, db_session=None)
Получение типа прибора по серийному номеру.

## API изменения

### UserResponse
Добавлено поле `device_type` с информацией о типе прибора.

### Регистрация пользователей
При регистрации автоматически определяется тип прибора по серийному номеру и устанавливается связь.

## Обратная совместимость

- Старая функция валидации сохранена как `validate_serial_number_static()`
- Если БД недоступна, используется статическая валидация
- Существующие пользователи не затронуты (поле `device_type_id` может быть NULL)

## Тестирование

```python
# Пример тестирования
from database import validate_serial_number, get_device_type_by_serial, get_db

# Тест валидации
assert validate_serial_number("SE0260001") == True
assert validate_serial_number("G6001") == True
assert validate_serial_number("INVALID123") == False

# Тест получения типа прибора
db = next(get_db())
device_type = get_device_type_by_serial("SE0260001", db)
assert device_type.name == "SE02"
```
