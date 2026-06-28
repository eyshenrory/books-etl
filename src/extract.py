import requests
from bs4 import BeautifulSoup


def extract_task(url: str):
    books_list = []

    for page in range(1, 51):
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Ошибка при запросе к сайту: {e}")        

        soup = BeautifulSoup(response.text, "html.parser")

        books = soup.find_all("article", class_="product_pod")

        for book in books: 
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            rating = book.find("p", class_="star-rating")["class"][1]

            books_list.append({
                "title": title,
                "price": price,
                "rating": rating
            }) 
            
    return books_list

if __name__ == "__main__":
    url = "https://books.toscrape.com/"
    data = extract_task(url)
    print(data[:3])
