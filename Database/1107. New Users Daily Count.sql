WITH first_login AS
(SELECT user_id
	,MIN(activity_date) as first_login
FROM traffic
WHERE activity = 'login'
GROUP BY user_id)
SELECT  login_date
	,COUNT(user_id) AS user_count
FROM traffic AS a 
INNER JOIN first_login AS b
ON a.user_id = b.user_id AND DATADIFF(day, b.first_login, sysdate)<90 AND a.activity = 'login'
GROUP BY login_date;