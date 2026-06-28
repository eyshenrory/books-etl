from pathlib import Path 
import pandas as pd 
from src.connect_db import get_connection


def run_query(filename: str) -> pd.DataFrame:
    sql_path = Path("sql") / filename

    with open(sql_path, encoding="utf-8") as f:
        query = f.read()

    conn = get_connection()

    try:
        df = pd.read_sql(query, conn)
    finally:
        conn.close()

    return df 

if __name__ == "__main__":
    df = run_query(input("Enter the name of the query file: "))
    print(f"\n{df.to_string(index=False)}")
