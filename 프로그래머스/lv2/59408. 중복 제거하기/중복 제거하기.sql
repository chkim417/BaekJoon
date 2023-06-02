-- 코드를 입력하세요
with A as
(
    select NAME FROM ANIMAL_INS
    WHERE NAME is not null
    group by NAME
)

select count(*)as count FROM A
