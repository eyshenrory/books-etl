import psycopg2
from src.connect_db import get_connection


def load_task(data: list):
    conn = get_connection()
    cur = conn.cursor()

    for item in data:

        cur.execute(
            """
            INSERT INTO books(title, rating)
            VALUES (%s, %s)
            ON CONFLICT (title)
            DO UPDATE SET rating = EXCLUDED.rating
            RETURNING id
            """,
            (item["title"], item["rating"])
        )

        book_id = cur.fetchone()[0]

        cur.execute(
            """
            INSERT INTO book_prices(book_id, price, scraped_at)
            VALUES (%s, %s, NOW())
            ON CONFLICT (book_id)
            DO UPDATE SET price = EXCLUDED.price, scraped_at = EXCLUDED.scraped_at
            """,
            (book_id, item["price"])
        )

    conn.commit()
    cur.close()
    conn.close()
