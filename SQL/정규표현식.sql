-- 코드를 입력하세요
SELECT  (
    CASE 
    WHEN SUBSTRING(ORDER_ID,-2,2) <= 10
    THEN REPLACE(ORDER_ID,SUBSTRING(ORDER_ID,-2,2),LPAD(SUBSTRING(ORDER_ID,-2,2),4,0))
    -- RPAD 로 오른쪽 자릿수를 채울 수도 있음!
    WHEN SUBSTRING(ORDER_ID,-2,2) <= 100 AND SUBSTRING(ORDER_ID,-2,2) > 10
    THEN REPLACE(ORDER_ID,SUBSTRING(ORDER_ID,-3,3),LPAD(SUBSTRING(ORDER_ID,-3,3),4,0))
    END
) AS 출고여부
FROM FOOD_ORDER

SELECT *
FROM FOOD_ORDER
WHERE ORDER_ID REGEXP "[0-9]{6,6}";

-- 정규식 리스트
. : 문자 하나
* : 앞 글자의 *개수 숫자 이상 반복
^ : 첫값
$ : 끝값
[.] : 괄호 안의 문자열 일치 확인
{.} : 반복
| : or
{m,n} : m번 이상 n번 이하