import matplotlib.pyplot as plt 
from analytics.queries import run_query


df = run_query("avg_price_by_rating.sql")

plt.figure(figsize=(8, 5))
plt.bar(df["rating"], df["average_price"])

plt.title("Average books prices by rating")
plt.xlabel("Rating")
plt.ylabel("Average books price")

plt.tight_layout()
plt.show()
