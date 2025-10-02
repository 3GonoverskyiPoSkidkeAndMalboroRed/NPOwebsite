# Нормативные документы - API и база данных

## Описание

Модуль для работы с нормативными документами (ГОСТы и стандарты) в системе НПО «СПЕКТРОН». Позволяет управлять базой данных нормативных документов через REST API.

## Структура базы данных

### Таблица `regulations`

| Поле | Тип | Описание |
|------|-----|----------|
| `id` | Integer | Уникальный идентификатор |
| `code` | String | Код ГОСТ (например, "ГОСТ Р 53203-2022") |
| `title` | String | Название документа |
| `company` | String | Компания-разработчик |
| `category` | String | Категория документа |
| `year` | String | Год издания |
| `description` | Text | Описание документа (опционально) |
| `file_path` | String | Путь к файлу документа (опционально) |
| `is_active` | Integer | Статус активности (1 - активен, 0 - неактивен) |
| `created_at` | DateTime | Дата создания записи |
| `updated_at` | DateTime | Дата последнего обновления |

## API Endpoints

### Получение списка документов
```
GET /regulations/
GET /regulations/?category=Сера
GET /regulations/?search=серы
GET /regulations/?is_active=1
```

**Параметры запроса:**
- `category` - фильтр по категории
- `search` - поиск по коду, названию или категории
- `is_active` - фильтр по активности (1 - активные, 0 - неактивные)

### Получение документа по ID
```
GET /regulations/{id}
```

### Создание документа
```
POST /regulations/
Content-Type: application/json

{
  "code": "ГОСТ Р 53203-2022",
  "title": "Определение серы методом рентгенофлуоресцентной спектрометрии",
  "company": "Спектрон",
  "category": "Сера",
  "year": "2022",
  "description": "Описание документа"
}
```

### Обновление документа
```
PUT /regulations/{id}
Content-Type: application/json

{
  "title": "Новое название",
  "description": "Новое описание"
}
```

### Удаление документа (мягкое удаление)
```
DELETE /regulations/{id}
```

### Получение категорий
```
GET /regulations/categories/list
```

### Получение статистики
```
GET /regulations/stats/summary
```

**Ответ:**
```json
{
  "total": 13,
  "categories": 8,
  "modern": 3
}
```

## Установка и настройка

### 1. Создание таблиц

Таблицы создаются автоматически при запуске приложения благодаря `Base.metadata.create_all(bind=engine)` в `database.py`.

### 2. Заполнение тестовыми данными

```bash
cd backend
python scripts/populate_regulations.py
```

### 3. Переменные окружения

Убедитесь, что в файле `.env` или переменных окружения установлены:

```env
DATABASE_URL=postgresql://user:password@db:5432/npo_db
VITE_API_URL=http://localhost:8000
```

## Frontend интеграция

### Composable useRegulations

```typescript
import { useRegulations } from '@/composables/useRegulations'

const {
  regulations,
  categories,
  stats,
  loading,
  error,
  filteredRegulations,
  sortedRegulations,
  setCategory,
  setSearch,
  resetFilters,
  initializeData
} = useRegulations()
```

### Типы TypeScript

```typescript
interface Regulation {
  id: number
  code: string
  title: string
  company: string
  category: string
  year: string
  description?: string
  file_path?: string
  is_active: number
  created_at: string
  updated_at: string
}
```

## Примеры использования

### Получение всех активных документов
```javascript
const response = await fetch('/regulations/?is_active=1')
const regulations = await response.json()
```

### Поиск документов по категории
```javascript
const response = await fetch('/regulations/?category=Сера')
const regulations = await response.json()
```

### Поиск документов по тексту
```javascript
const response = await fetch('/regulations/?search=серы')
const regulations = await response.json()
```

### Создание нового документа
```javascript
const newRegulation = {
  code: "ГОСТ Р 12345-2023",
  title: "Новый стандарт",
  company: "Спектрон",
  category: "Металлы",
  year: "2023",
  description: "Описание нового стандарта"
}

const response = await fetch('/regulations/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(newRegulation)
})
```

## Категории документов

- Сера
- Металлы
- Сталь
- Алюминий
- Свинец
- Бронзы
- Латуни
- Хлорорганические соединения
- Топлива

## Особенности

1. **Мягкое удаление**: Документы не удаляются физически, а помечаются как неактивные (`is_active = 0`)
2. **Автоматическая сортировка**: Документы сортируются по году (новые сначала)
3. **Поиск**: Поддерживается поиск по коду, названию и категории
4. **Фильтрация**: Возможна фильтрация по категории и статусу активности
5. **Статистика**: API предоставляет статистику по количеству документов, категорий и современных документов
