SELECT 
  b.rating,
  round(AVG(p.price), 1) AS average_price
FROM
  books b
JOIN 
  book_prices p ON b.id = p.book_id
GROUP BY
  b.rating
ORDER BY 
  b.rating desc;
