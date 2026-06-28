def transform_task(books: list):
    cleaned = []

    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    for book in books:
        try:
            price = float(book["price"].replace("Â£", ""))
            rating = rating_map.get(book["rating"], None)

            cleaned.append({
                "title": book["title"],
                "price": price,
                "rating": rating
            })
        except Exception as e:
            print(f"Skipping row: {e}")

    return cleaned

