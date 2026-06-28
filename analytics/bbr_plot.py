import matplotlib.pyplot as plt 
from analytics.queries import run_query


df = run_query("books_by_rating.sql")

plt.figure(figsize=(8, 5))
plt.bar(df["rating"], df["books_count"])

plt.title("Books count by rating")
plt.xlabel("Rating")
plt.ylabel("Books count")

plt.tight_layout()
plt.show()
