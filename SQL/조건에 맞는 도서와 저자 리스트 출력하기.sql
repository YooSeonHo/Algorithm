-- 코드를 입력하세요
SELECT b.BOOK_ID, a.AUTHOR_NAME, DATE_FORMAT(b.PUBLISHED_DATE,'%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK b, AUTHOR a
WHERE b.author_id = a.author_id and b.category = '경제'
ORDER BY b.PUBLISHED_DATE