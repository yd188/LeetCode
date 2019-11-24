/*
The Trips table holds all taxi trips. Each trip has a unique Id, while Client_Id and Driver_Id are both foreign keys to the Users_Id at the Users table. Status is an ENUM type of ('completed', 'cancelled_by_driver', 'cancelled_by_client').

+----+-----------+-----------+---------+--------------------+----------+
| Id | Client_Id | Driver_Id | City_Id |        Status      |Request_at|
+----+-----------+-----------+---------+--------------------+----------+
| 1  |     1     |    10     |    1    |     completed      |2013-10-01|
| 2  |     2     |    11     |    1    | cancelled_by_driver|2013-10-01|
| 3  |     3     |    12     |    6    |     completed      |2013-10-01|
| 4  |     4     |    13     |    6    | cancelled_by_client|2013-10-01|
| 5  |     1     |    10     |    1    |     completed      |2013-10-02|
| 6  |     2     |    11     |    6    |     completed      |2013-10-02|
| 7  |     3     |    12     |    6    |     completed      |2013-10-02|
| 8  |     2     |    12     |    12   |     completed      |2013-10-03|
| 9  |     3     |    10     |    12   |     completed      |2013-10-03| 
| 10 |     4     |    13     |    12   | cancelled_by_driver|2013-10-03|
+----+-----------+-----------+---------+--------------------+----------+
The Users table holds all users. Each user has an unique Users_Id, and Role is an ENUM type of ('client', 'driver', 'partner').

+----------+--------+--------+
| Users_Id | Banned |  Role  |
+----------+--------+--------+
|    1     |   No   | client |
|    2     |   Yes  | client |
|    3     |   No   | client |
|    4     |   No   | client |
|    10    |   No   | driver |
|    11    |   No   | driver |
|    12    |   No   | driver |
|    13    |   No   | driver |
+----------+--------+--------+
Write a SQL query to find the cancellation rate of requests made by unbanned users (both client and driver must be unbanned) between Oct 1, 2013 and Oct 3, 2013. The cancellation rate is computed by dividing the number of canceled (by client or driver) requests made by unbanned users by the total number of requests made by unbanned users.

For the above tables, your SQL query should return the following rows with the cancellation rate being rounded to two decimal places.

+------------+-------------------+
|     Day    | Cancellation Rate |
+------------+-------------------+
| 2013-10-01 |       0.33        |
| 2013-10-02 |       0.00        |
| 2013-10-03 |       0.50        |
+------------+-------------------+

Note: hash(#) means temporary in Redshift
Solution:
*/

WITH total AS
(SELECT t.request_at
        ,COUNT(t.id) AS counts
FROM trips AS t
INNER JOIN users AS c
ON t.client_id = c.user_id AND c.banned != 'Yes'
INNER JOIN #users AS d
ON t.client_id = d.user_id AND d.banned != 'Yes'
GROUP BY t.request_at)
, cancelled AS 
(SELECT t2.request_at
        ,COUNT(t2.id) AS counts
FROM trips AS t2
INNER JOIN #users AS c2
ON t2.client_id = c2.user_id AND c2.banned != 'Yes'
INNER JOIN #users AS d
ON t2.client_id = d2.user_id AND d2.banned != 'Yes'
WHERE t2.status IN ('cancelled_by_driver', 'cancelled_by_client')
GROUP BY t2.request_at)
SELECT total.request_at AS day
      ,CASE WHEN cancelled.counts/total.counts:: NUMERIC(18,2) IS NULL THEN 0.00 ELSE cancelled.counts/total.counts:: NUMERIC(18,2) END AS cancellation_rate
FROM total AS totoal
LEFT JOIN cancelled AS cancelled
ON total.request_at = cancelled.request_at
ORDER BY day;
