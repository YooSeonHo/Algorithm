-- 코드를 입력하세요

SELECT COUNT(DISTINCT(NAME)) AS count
FROM ANIMAL_INS
WHERE NAME is not null

# SELECT COUNT(*) AS count
# FROM ANIMAL_INS a1, ANIMAL_INS a2
# WHERE a1.ANIMAL_ID != a2.ANIMAL_ID and a1.NAME = a2.NAME