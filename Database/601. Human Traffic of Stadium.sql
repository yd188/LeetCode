/*
X city built a new stadium, each day many people visit it and the stats are saved as these columns: id, visit_date, people

Please write a query to display the records which have 3 or more consecutive rows and the amount of people more than 100(inclusive).

For example, the table stadium:
+------+------------+-----------+
| id   | visit_date | people    |
+------+------------+-----------+
| 1    | 2017-01-01 | 10        |
| 2    | 2017-01-02 | 109       |
| 3    | 2017-01-03 | 150       |
| 4    | 2017-01-04 | 99        |
| 5    | 2017-01-05 | 145       |
| 6    | 2017-01-06 | 1455      |
| 7    | 2017-01-07 | 199       |
| 8    | 2017-01-08 | 188       |
+------+------------+-----------+
For the sample data above, the output is:

+------+------------+-----------+
| id   | visit_date | people    |
+------+------------+-----------+
| 5    | 2017-01-05 | 145       |
| 6    | 2017-01-06 | 1455      |
| 7    | 2017-01-07 | 199       |
| 8    | 2017-01-08 | 188       |
+------+------------+-----------+
*/

WITH TEMP AS
(SELECT  a.id
	,b.id AS id2
	,c.id AS id3
	,a.visit_date
	,a.people
FROM stadium AS A
INNER JOIN stadium AS b
ON a.id = b.id-1 and b.people > 100
INNER JOIN stadium AS C
ON a.id = C.id-2 and C.people > 100)
, get_id AS
(SELECT id FROM TEMP
UNION
SELECT id2 AS id 
FROM TEMP
UNION 
SELECT id3 AS id 
FROM TEMP)
SELECT d.* 
FROM TEMP AS d
INNER JOIN get_id as e 
ON d.id = e.id
ORDER BY id;
