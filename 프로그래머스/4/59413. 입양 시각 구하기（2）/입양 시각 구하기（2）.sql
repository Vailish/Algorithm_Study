-- 코드를 입력하세요
# SELECT
# HOUR(DATETIME) AS `HOUR`,
# IFNULL(COUNT(DATETIME), 0) AS `COUNT`
# FROM ANIMAL_OUTS
# GROUP BY HOUR(DATETIME)
# ORDER BY HOUR
# ;

WITH RECURSIVE CTE AS (
    SELECT 0 AS NUM
    UNION ALL
    SELECT NUM+1 FROM CTE
    WHERE NUM < 23
)

SELECT
NUM,
IFNULL(O.C, 0) AS `COUNT`
FROM CTE
LEFT JOIN
(SELECT HOUR(DATETIME) AS TIME, COUNT(DATETIME) AS C FROM ANIMAL_OUTS GROUP BY TIME) AS O
ON O.TIME = CTE.NUM
ORDER BY NUM
;

