-- # Write your MySQL query statement below
-- SELECT NAME,AREA,POPULATION
-- FROM WORLD
-- WHILE AREA  >=3000000 OR POPULATION >=25000000;
SELECT name, population, area
FROM World
WHERE area >= 3000000 OR population >= 25000000;