import pandas as pd


def to_csv_task(data: list, output_path: str = "data/books.csv"):
    df = pd.DataFrame(data)
    df.to_csv(output_path, index=False, encoding="utf-8-sig")
    print(f"Saved to {output_path} | rows: {len(df)}")
