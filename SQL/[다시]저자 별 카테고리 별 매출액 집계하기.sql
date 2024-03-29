-- # -- 코드를 입력하세요
-- # SELECT b.AUTHOR_ID AS AUTHOR_ID, a.AUTHOR_NAME AS AUTHOR_NAME, b.CATEGORY AS CATEGORY, (b.PRICE * s.SALES) AS TOTAL_SALES
-- # FROM BOOK b, AUTHOR a, BOOK_SALES s
-- # WHERE b.AUTHOR_ID = a.AUTHOR_ID AND b.BOOK_ID = s.BOOK_ID 
-- #     AND DATE_FORMAT(s.SALES_DATE,'%Y-%m') = '2022-01' 
-- # GROUP BY AUTHOR_ID, CATEGORY
-- # ORDER BY AUTHOR_ID, CATEGORY DESC

SELECT AUTHOR_ID,AUTHOR_NAME,CATEGORY, SUM(TOTAL_SALES) AS TOTAL_SALES
FROM 
    (SELECT b.AUTHOR_ID AS AUTHOR_ID, a.AUTHOR_NAME AS AUTHOR_NAME, b.CATEGORY AS CATEGORY, (b.PRICE * s.SALES) AS TOTAL_SALES
    FROM BOOK b, AUTHOR a, BOOK_SALES s
    WHERE b.AUTHOR_ID = a.AUTHOR_ID AND b.BOOK_ID = s.BOOK_ID 
    AND DATE_FORMAT(s.SALES_DATE,'%Y-%m') = '2022-01') A
GROUP BY AUTHOR_ID, CATEGORY
ORDER BY AUTHOR_ID, CATEGORY DESC