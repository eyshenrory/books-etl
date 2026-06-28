import psycopg2


def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="prices",
        user="admin",
        password="admin",
        port=5432
    )

