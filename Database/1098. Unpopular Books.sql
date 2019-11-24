WITH total_ordered AS
(SELECT  a.book_id
	,a.name
	,SUM(NVL(b.quantity,0)) AS ordered
FROM books AS a
LEFT JOIN orders AS b
--ON a.book_id=b.book_id AND a.available_from<DATEADD(day,-30,sysdate)
ON a.book_id=b.book_id AND DATEDIFF(day, a.available_from , sysdate)>30
GROUP BY a.name)
SELECT  book_id
	,name
FROM total_ordered
WHERE ordered < 10;