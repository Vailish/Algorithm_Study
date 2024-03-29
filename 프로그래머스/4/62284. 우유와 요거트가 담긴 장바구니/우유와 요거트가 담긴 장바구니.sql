-- 코드를 입력하세요
# MILK가 있는 컬럼을 선택하고
# YOGURT가 있는 컬럼을 선택하고
# INTERSECT를 사용하여 둘다 있는 ID값을 가져온다
SELECT
T.CART_ID
FROM 
(
    SELECT CART_ID FROM CART_PRODUCTS WHERE NAME = 'Milk'
    INTERSECT
    SELECT CART_ID FROM CART_PRODUCTS WHERE NAME = 'Yogurt'
) AS T
ORDER BY T.CART_ID
;
