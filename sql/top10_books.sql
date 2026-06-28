WITH rtable AS (
  SELECT
    b.title,
    p.price,
    DENSE_RANK() OVER(ORDER BY p.price DESC) rn 
  FROM 
    books b 
  JOIN
    book_prices p ON b.id = p.book_id
)

SELECT 
  title, 
  round(price, 1) AS price
FROM 
  rtable 
WHERE 
  rn <= 10;
