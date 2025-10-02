# Docker Configuration для NPO Website

## Режимы работы

### 🚀 Режим разработки (по умолчанию)
```bash
# Запуск в dev-режиме с auto-reload
docker-compose up

# Или явно указать dev-файл
docker-compose -f docker-compose.dev.yml up
```

**Особенности dev-режима:**
- ✅ **Backend**: Auto-reload при изменении Python файлов
- ✅ **Frontend**: Hot-reload при изменении Vue/TypeScript файлов
- ✅ **Volumes**: Исходный код монтируется в контейнеры
- ✅ **Порты**: 
  - Backend: http://localhost:8000
  - Frontend: http://localhost:3000
  - Database: localhost:5432

### 🏭 Продакшен режим
```bash
# Запуск в продакшен режиме
docker-compose -f docker-compose.prod.yml up
```

**Особенности prod-режима:**
- ✅ **Backend**: Оптимизированная сборка без dev-зависимостей
- ✅ **Frontend**: Собранное приложение через nginx
- ✅ **Без volumes**: Код копируется в контейнеры при сборке
- ✅ **Порты**: 
  - Backend: http://localhost:8000
  - Frontend: http://localhost:3000
  - Nginx: http://localhost:8081

## Команды для разработки

### Запуск всех сервисов
```bash
# Dev режим (рекомендуется для разработки)
docker-compose up

# Prod режим
docker-compose -f docker-compose.prod.yml up
```

### Запуск в фоновом режиме
```bash
# Dev режим
docker-compose up -d

# Prod режим
docker-compose -f docker-compose.prod.yml up -d
```

### Пересборка контейнеров
```bash
# Dev режим
docker-compose up --build

# Prod режим
docker-compose -f docker-compose.prod.yml up --build
```

### Остановка сервисов
```bash
# Остановка всех сервисов
docker-compose down

# Остановка с удалением volumes
docker-compose down -v
```

## Структура файлов

```
├── docker-compose.yml          # Dev режим (по умолчанию)
├── docker-compose.dev.yml      # Dev режим (явно)
├── docker-compose.prod.yml     # Prod режим
├── frontend/
│   ├── Dockerfile              # Prod сборка фронтенда
│   └── Dockerfile.dev          # Dev сборка фронтенда
└── backend/
    └── Dockerfile               # Backend (dev + prod)
```

## Auto-reload настройки

### Backend (FastAPI)
- **Файл**: `backend/Dockerfile`
- **Команда**: `uvicorn main:app --reload`
- **Volume**: `./backend:/app`
- **Автоперезагрузка**: При изменении `.py` файлов

### Frontend (Vue.js + Vite)
- **Файл**: `frontend/Dockerfile.dev`
- **Команда**: `npm run dev -- --host 0.0.0.0 --port 5173`
- **Volume**: `./frontend:/app`
- **Hot-reload**: При изменении `.vue`, `.ts`, `.js` файлов
- **Polling**: `CHOKIDAR_USEPOLLING=true` для Windows

## Устранение проблем

### Проблемы с hot-reload на Windows
Если hot-reload не работает на Windows, убедитесь что:
1. В `docker-compose.yml` установлена переменная `CHOKIDAR_USEPOLLING=true`
2. Volume mapping настроен правильно: `./frontend:/app`

### Проблемы с портами
Если порты заняты, измените их в `docker-compose.yml`:
```yaml
ports:
  - "0.0.0.0:3001:5173"  # Изменить 3000 на 3001
```

### Очистка Docker
```bash
# Удаление всех контейнеров и volumes
docker-compose down -v
docker system prune -a

# Пересборка с нуля
docker-compose up --build --force-recreate
```
