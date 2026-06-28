# 📊 Books ETL Project

## 📌 Описание проекта

Этот проект представляет собой ETL-пайплайн, который собирает данные о книгах с сайта, обрабатывает их и сохраняет в PostgreSQL для дальнейшего анализа.

Проект демонстрирует базовые принципы работы Data Engineer:

- сбор данных (web scraping)
- обработка данных (transform)
- загрузка в БД (load)
- аналитика через SQL
- визуализация данных в Python

---

## ⚙️ Архитектура проекта


Сайт (Books to Scrape) -> Python ETL (Extract → Transform → Load) -> PostgreSQL (хранение данных) -> SQL-запросы (аналитика) -> Python (pandas + matplotlib)


---

## 🧱 Используемые технологии

- Python
- PostgreSQL
- psycopg2
- Pandas
- BeautifulSoup
- Matplotlib
- Docker

---

## 🗂 Структура базы данных

### 📘 Таблица books
Хранит информацию о книгах:

- id (Первичный ключ)
- title
- rating

### 💰 Таблица book_prices
Хранит историю цен:

- book_id (Внешний ключ)
- price
- scraped_at

---

## 🚀 Как запустить проект

### 
```
1. Запуск базы данных
$ docker-compose up -d
2. Инициализация данных 
$ python -m src.main
3. Запуск аналитики
$ python -m analytics."имя_файла"
```
## 📊 Примеры аналитики

Проект позволяет получать следующие инсайты:

- самые дорогие книги
- распределение количества книг по рейтингу
- распределение средней цены книг по рейтингу

## 🖥️ Примеры SQL-запросов
```
-- Топ-10 самых дорогих книг
WITH rtable AS (
  SELECT
    b.title,
    p.price,
    DENSE_RANK() OVER(ORDER BY p.price DESC) rn 
  FROM 
    books b 
  JOIN
    book_prices p ON b.id = p.book_id
)

SELECT
  title, 
  round(price, 1) AS price
FROM 
  rtable 
WHERE 
  rn <= 10;

-- Распределение количества книг по рейтингу
SELECT 
  rating,
  COUNT(*) AS books_count
FROM 
  books 
GROUP BY 
  rating 
ORDER BY   
  rating DESC;
```

## 📈 Пример визуализации

Распределение рейтингов

<img width="795" height="502" alt="{45EA1B26-3A9D-479F-BDF2-10A7C9810D5E}" src="https://github.com/user-attachments/assets/484d491a-d375-496c-b150-8c8b08315745" />

(строится через matplotlib + pandas)

## 🔥 Особенности проекта
- реализован полноценный ETL-пайплайн
- используется PostgreSQL как хранилище данных
- реализована история цен (time-series данные)
- SQL используется для аналитики
- Python используется для визуализации
  
## 📦 Помимо хранения данных в PostgreSQL, проект поддерживает экспорт данных в CSV-формат для:
- передачи данных
- локального анализа
- резервного копирования
- использования в BI-инструментах
