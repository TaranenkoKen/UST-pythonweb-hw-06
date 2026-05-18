# UST Python Web HW-06

## 📌 Опис проєкту

Цей проєкт реалізує базу даних університету з використанням:

- PostgreSQL (через Docker)
- SQLAlchemy ORM
- Alembic (міграції)
- Faker (заповнення тестовими даними)

База даних містить студентів, групи, викладачів, предмети та оцінки.

---

## ⚙️ Технології

- Python 3.x
- PostgreSQL
- SQLAlchemy
- Alembic
- Faker
- Docker

## Структура проекту

```
hw06/
├── alembic.ini              # Конфігурація Alembic
├── database.py              # Налаштування підключення до БД
├── models.py                # SQLAlchemy-моделі
├── seed.py                  # Наповнення БД тестовими даними
├── my_select.py             # 10 функцій вибірки (select_1 … select_10)
├── requirements.txt
```

## Запуск

### 1. Запустити PostgreSQL у Docker

```bash
docker run --name neoversity-db -p 5432:5432 -e POSTGRES_PASSWORD=12345 -d postgres
```

### 2. Встановити залежності

```bash
pip install -r requirements.txt
```

### 3. Застосувати міграції

```bash
alembic upgrade head
```

### 4. Заповнити базу даних

```bash
python seed.py
```

### 5. Виконати запити

```bash
python my_select.py
```
