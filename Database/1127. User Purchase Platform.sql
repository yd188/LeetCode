/*
Table: Spending

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| user_id     | int     |
| spend_date  | date    |
| platform    | enum    | 
| amount      | int     |
+-------------+---------+
The table logs the spendings history of users that make purchases from an online shopping website which has a desktop and a mobile application.
(user_id, spend_date, platform) is the primary key of this table.
The platform column is an ENUM type of ('desktop', 'mobile').
Write an SQL query to find the total number of users and the total amount spent using mobile only, desktop only and both mobile and desktop together for each date.

The query result format is in the following example:

Spending table:
+---------+------------+----------+--------+
| user_id | spend_date | platform | amount |
+---------+------------+----------+--------+
| 1       | 2019-07-01 | mobile   | 100    |
| 1       | 2019-07-01 | desktop  | 100    |
| 2       | 2019-07-01 | mobile   | 100    |
| 2       | 2019-07-02 | mobile   | 100    |
| 3       | 2019-07-01 | desktop  | 100    |
| 3       | 2019-07-02 | desktop  | 100    |
+---------+------------+----------+--------+

Result table:
+------------+----------+--------------+-------------+
| spend_date | platform | total_amount | total_users |
+------------+----------+--------------+-------------+
| 2019-07-01 | desktop  | 100          | 1           |
| 2019-07-01 | mobile   | 100          | 1           |
| 2019-07-01 | both     | 200          | 1           |
| 2019-07-02 | desktop  | 100          | 1           |
| 2019-07-02 | mobile   | 100          | 1           |
| 2019-07-02 | both     | 0            | 0           |
+------------+----------+--------------+-------------+ 
On 2019-07-01, user 1 purchased using both desktop and mobile, user 2 purchased using mobile only and user 3 purchased using desktop only.
On 2019-07-02, user 2 purchased using mobile only, user 3 purchased using desktop only and no one purchased using both platforms.
*/


WITH get_date AS
(SELECT DISTINCT spend_date 
FROM spendings)
, get_both AS
(SELECT  b.spend_date
	,'both' AS platform
	,SUM(NVL(a.sum_amount,0)) AS total_amount
	,COUNT(a.user_id) AS total_users
FROM(SELECT  spend_date
	,user_id
	,SUM(amount) AS sum_amount
	FROM spendings
	GROUP BY 1, 2
	HAVING COUNT(platform)=2) AS a
RIGHT JOIN get_date AS b 
ON a.spend_date = b.spend_date
GROUP BY 1, 2)
, get_mobile AS
(SELECT  d.spend_date
	,'mobile' AS platform
	,SUM(NVL(c.sum_amount,0)) AS total_amount
	,COUNT(c.user_id) AS total_users
FROM(SELECT  spend_date
	,user_id
	,SUM(amount) AS sum_amount
	FROM spendings
	WHERE platform = 'mobile'
	GROUP BY 1, 2
	HAVING COUNT(platform)<2) AS c
RIGHT JOIN get_date AS d 
ON c.spend_date = d.spend_date
GROUP BY 1, 2)
, get_desktop AS
(SELECT  f.spend_date
	,'mobile' AS platform
	,SUM(NVL(e.sum_amount,0)) AS total_amount
	,COUNT(e.user_id) AS total_users
FROM(SELECT  spend_date
	,user_id
	,SUM(amount) AS sum_amount
	FROM spendings
	WHERE platform = 'desktop'
	GROUP BY 1, 2
	HAVING COUNT(platform)<2) AS e
RIGHT JOIN get_date AS f 
ON e.spend_date = f.spend_date
GROUP BY 1, 2)
SELECT * FROM get_both
UNION ALL
SELECT * FROM get_mobile
UNION ALL
SELECT * FROM get_desktop
ORDER BY spend_date, platform;
