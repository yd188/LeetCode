/*
Write a SQL query to find all numbers that appear at least three times consecutively.

+----+-----+
| Id | Num |
+----+-----+
| 1  |  1  |
| 2  |  1  |
| 3  |  1  |
| 4  |  2  |
| 5  |  1  |
| 6  |  2  |
| 7  |  2  |
+----+-----+
For example, given the above Logs table, 1 is the only number that appears consecutively for at least three times.

+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
*/

SELECT a.num AS consecutiveNums
FROM logs AS a
INNER JOIN log AS b
ON a.id=b.id-1 AND a.num=b.num
INNER JOIN log AS c
ON a.id=c.id-2 AND a.num=c.num;
