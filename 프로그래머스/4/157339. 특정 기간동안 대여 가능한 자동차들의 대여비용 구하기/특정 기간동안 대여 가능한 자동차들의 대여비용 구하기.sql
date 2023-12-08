-- 코드를 입력하세요
SELECT
C.CAR_ID,
C.CAR_TYPE,
ROUND(30 * C.DAILY_FEE * (1 - (
    SELECT DISCOUNT_RATE
    FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS P
    WHERE P.DURATION_TYPE = "30일 이상" AND C.CAR_TYPE = P.CAR_TYPE
)/100), 0) AS FEE
FROM CAR_RENTAL_COMPANY_CAR AS C
LEFT JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS H
ON C.CAR_ID = H.CAR_ID
WHERE C.CAR_TYPE IN ("세단", "SUV")
AND C.CAR_ID NOT IN (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE START_DATE <= "2022-11-01" AND END_DATE >= "2022-11-01")
GROUP BY C.CAR_ID
HAVING FEE >= 500000 AND FEE < 2000000
ORDER BY FEE DESC, C.CAR_TYPE, CAR_ID DESC
;