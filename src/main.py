from src.pipeline import run_pipeline
from src.init_db import init_db


def main():
    print("INIT DB")
    init_db()

    print("RUN PIPELINE")
    run_pipeline()

    print("DONE")
    
    

if __name__ == "__main__":
    main()

