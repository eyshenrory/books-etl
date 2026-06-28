SELECT 
  rating,
  COUNT(*) AS books_count
FROM 
  books 
GROUP BY 
  rating 
ORDER BY 
  rating DESC;
