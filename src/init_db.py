import psycopg2
from datetime import datetime

def init_db():
    conn = psycopg2.connect(
        host="localhost",
        database="prices",
        user="admin",
        password="admin",
        port=5432
    )

    cur = conn.cursor()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS books (
            id SERIAL PRIMARY KEY,
            title TEXT UNIQUE NOT NULL,
            rating INT
        );

        CREATE TABLE IF NOT EXISTS book_prices (
            book_id SERIAL PRIMARY KEY,
            price NUMERIC,
            scraped_at TIMESTAMP DEFAULT NOW()
        );
        """
        )

    conn.commit()
    cur.close()
    conn.close()

    print("DB initialized")

if __name__ == "__main__":
    init_db()
