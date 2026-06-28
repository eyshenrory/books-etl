from src.extract import extract_task
from src.transform import transform_task
from src.load import load_task
from src.to_csv import to_csv_task


def run_pipeline():
    url = "https://books.toscrape.com/"

    print("Extracting...")
    raw = extract_task(url)
    print(f"  Extracted: {len(raw)} books")

    print("Transforming...")
    clean = transform_task(raw)
    print(f"  After transform: {len(clean)} books")

    print("Loading...")
    load_task(clean)
    print(f"  Inserted: {len(clean)} books")

    to_csv_task(clean)

if __name__ == "__main__":
    run_pipeline()
