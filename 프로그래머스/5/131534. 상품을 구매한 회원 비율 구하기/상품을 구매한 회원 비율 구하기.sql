-- 코드를 입력하세요
SELECT
YEAR(SALES_DATE) AS YEAR,
MONTH(SALES_DATE) AS MONTH,
COUNT(DISTINCT S.USER_ID) AS PUCHASED_USERS,
ROUND(COUNT(DISTINCT S.USER_ID)/(
    SELECT COUNT(USER_ID)
    FROM USER_INFO
    WHERE YEAR(JOINED) = 2021
), 1) AS PUCHASED_RATIO
FROM USER_INFO AS I
INNER JOIN ONLINE_SALE AS S ON I.USER_ID = S.USER_ID
WHERE YEAR(JOINED) = 2021
GROUP BY YEAR(SALES_DATE), MONTH(SALES_DATE)
ORDER BY YEAR, MONTH
;