-- 코드를 입력하세요
SELECT  ANIMAL_ID, NAME, IF(SEX_UPON_INTAKE Like '%Spayed%'OR SEX_UPON_INTAKE Like '%Neutered%', 'O', 'X') as 중성화 
FROM ANIMAL_INS
ORDER BY ANIMAL_ID ASC