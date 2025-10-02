# Динамические методики - Инструкция по настройке

## Описание

Система динамических методик позволяет загружать информацию о методиках анализа из базы данных вместо использования статических данных в frontend.

## Структура

### Backend
- **Таблица `methods`** - основная таблица для хранения методик
- **API endpoints** - REST API для работы с методиками
- **Миграция данных** - скрипты для заполнения БД

### Frontend
- **Composable `useMethods`** - логика работы с API
- **Обновленный компонент `Methods.vue`** - динамическая загрузка данных
- **Обновленный `MethodBlock.vue`** - передача ID методик

## Установка и настройка

### 1. Запуск миграции данных

Есть несколько способов запуска миграции:

#### Способ 1: Автоматический (рекомендуется)
```bash
cd backend
python run_migration.py
```

#### Способ 2: Через Docker
```bash
# Запустить контейнеры
docker-compose up -d

# Выполнить миграцию
cd backend
python migrate_methods_docker.py
```

#### Способ 3: Локально (если PostgreSQL установлен локально)
```bash
cd backend
python migrate_methods_local.py
```

#### Способ 4: Ручная миграция через SQL
```bash
# Подключиться к PostgreSQL и выполнить:
psql -h localhost -U user -d npo_db -f manual_migration.sql
```

### 2. Настройка переменных окружения

Создайте файл `.env` в папке `frontend`:

```env
VITE_API_URL=http://localhost:8000
```

### 3. Запуск приложения

```bash
# Backend
cd backend
python main.py

# Frontend
cd frontend
npm run dev
```

## API Endpoints

### Получение списка методик
```
GET /methods
GET /methods?category=oil
GET /methods?is_active=1
```

### Получение методики по ID
```
GET /methods/{id}
```

### Создание методики
```
POST /methods
```

### Обновление методики
```
PUT /methods/{id}
```

### Удаление методики (мягкое удаление)
```
DELETE /methods/{id}
```

### Получение категорий
```
GET /methods/categories/list
```

## Структура данных методики

```json
{
  "id": 1,
  "title": "Название методики",
  "standards_description": "Описание стандартов",
  "method_description": "Описание метода",
  "description_content": ["Пункт 1", "Пункт 2"],
  "limitations": "Ограничения метода",
  "procedure": ["Шаг 1", "Шаг 2"],
  "documentation": [
    {
      "title": "Название документа",
      "description": "Описание",
      "link": "Ссылка"
    }
  ],
  "equipment": [
    {
      "name": "Название оборудования",
      "description": "Описание",
      "specifications": "Характеристики"
    }
  ],
  "category": "oil",
  "is_active": 1,
  "created_at": "2024-01-01T00:00:00",
  "updated_at": "2024-01-01T00:00:00"
}
```

## Категории методик

- `oil` - Нефть и нефтепродукты
- `eco` - Экология
- `mining` - Горнорудная промышленность
- `metallurgy` - Металлургия
- `diagnostics` - Диагностика и контроль
- `gas` - Газовая промышленность

## Добавление новых методик

1. Используйте API endpoint `POST /methods`
2. Или добавьте данные напрямую в БД через SQL
3. Убедитесь, что указана правильная категория

## ✅ Статус реализации

Система динамических методик успешно реализована и протестирована:

- ✅ Таблица `methods` создана в БД
- ✅ API endpoints работают корректно
- ✅ Миграция данных выполнена (5 методик добавлено)
- ✅ Frontend обновлен для работы с API
- ✅ Docker контейнеры настроены

## Troubleshooting

### Ошибка подключения к API
- Проверьте, что backend запущен на порту 8000
- Убедитесь, что переменная `VITE_API_URL` настроена правильно
- Проверьте логи: `docker logs npo_backend`

### Ошибка загрузки данных
- Проверьте, что таблица `methods` создана
- Убедитесь, что данные мигрированы: `docker exec npo_backend python -c "from database import SessionLocal, Method; db = SessionLocal(); print(f'Методик в БД: {len(db.query(Method).all())}'); db.close()"`

### Ошибки TypeScript
- Убедитесь, что все типы импортированы правильно
- Проверьте совместимость типов между frontend и backend

### Проблемы с кодировкой
- Если возникают ошибки с эмодзи в скриптах, используйте `manual_migration.sql`
- Проверьте кодировку файлов (должна быть UTF-8)
