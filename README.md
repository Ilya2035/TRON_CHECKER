# 🚀 Tron Checker Service

Микросервис, который получает информацию об адресе в сети Tron: `bandwidth`, `energy` и баланс TRX. Каждый запрос сохраняется в базу данных. Реализован REST API с двумя эндпоинтами и поддержкой пагинации. При ошибке — возвращает корректные сообщения, если адрес не существует или данные невозможно обработать.

---

## 🛠 Стек технологий

- **FastAPI** — асинхронный веб-фреймворк  
- **TronPy** — клиент для взаимодействия с сетью Tron  
- **SQLAlchemy** — ORM для работы с базой данных  
- **SQLite (aiosqlite)** — лёгкая асинхронная БД  
- **Pydantic** — валидация и сериализация данных  
- **FastAPI Pagination** — готовая реализация пагинации  
- **Pytest** — тестирование (юнит и интеграционное)

---

## 📦 Установка и запуск

```bash
# Клонировать репозиторий
git clone https://github.com/Ilya2035/TRON_CHECKER.git
cd TRON_CHECKER

# Создать и активировать виртуальное окружение
python -m venv venv
source venv/bin/activate        # для Linux/macOS
venv\Scripts\activate           # для Windows

# Установить зависимости
pip install -r requirements.txt

# Создать .env и указать API ключ TronGrid
echo "API_KEY=your_tron_api_key" > .env

# Запустить приложение
uvicorn app.main:app --reload
```

## 🧪 Тестирование

```bash
# Запустить все тесты
pytest
```

Покрываются:
- Интеграционные тесты для POST и GET эндпоинтов
- Юнит-тест записи запроса в БД

---

## 📡 Примеры API-запросов

### ▶️ POST `/requests_for_tron/`

Создаёт запрос к Tron-сети для получения информации об адресе.

**Request body:**

```json
{
  "address": "TTVGXZS7h8r47dgEKpF62kEmb8NS8H2PwD"
}
```

**Response:**

```json
{
  "bandwidth": 600,
  "energy": 0,
  "balance_trx": 0.000015558539
}
```

**Curl:**

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/requests_for_tron/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "address": "TTVGXZS7h8r47dgEKpF62kEmb8NS8H2PwD"
}'
```

---

### ❗ Ошибки

Если адрес не найден в сети Tron:

```json
{
  "detail": "Tron account 'TXYZ...' not found or invalid: ..."
}
```

Если не удаётся обработать данные ресурса:

```json
{
  "detail": "Failed to parse resource info for address 'TXYZ...'"
}
```

Если формат адреса неверный:

```json
{
  "detail": [
    {
      "loc": ["body", "address"],
      "msg": "string does not match regex",
      "type": "value_error"
    }
  ]
}
```

---

### 📄 GET `/requests_for_tron/?page=1&size=50`

Получает список последних запросов с возможностью пагинации.

**Response:**

```json
{
  "items": [
    {
      "id": 1,
      "tron_address": "TTVGXZS7h8r47dgEKpF62kEmb8NS8H2PwD",
      "request_time": "2025-03-28T15:07:49"
    }
  ],
  "total": 1,
  "page": 1,
  "size": 50,
  "pages": 1
}
```

---

## 📁 Структура проекта

```
app/
├── clients/            # Tron клиент
├── crud/               # Работа с БД
├── database.py         # Подключение и сессии
├── main.py             # Точка входа приложения
├── models.py           # SQLAlchemy ORM модели
├── routers/            # API маршруты
├── schemas.py          # Pydantic-схемы
├── service/            # Логика получения данных
├── config.py           # Настройки TRX → SUN
└── settings.py         # Переменные из .env

tests/
├── test_requests.py    # Интеграционные тесты
├── test_db.py          # Юнит-тесты
```

---

## ✅ Возможности

- Получение информации по Tron-адресу
- Запись всех обращений в базу
- Обработка ошибок: невалидный адрес, отсутствие пользователя
- История запросов с пагинацией
- Покрытие ключевого функционала тестами

---

## 📬 Обратная связь

Если возникнут вопросы или предложения — fyrno2049@gmail.com
