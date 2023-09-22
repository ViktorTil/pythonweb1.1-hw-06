--Знайти які курси читає певний викладач.
SELECT t.fullname AS Teacher, d.name AS Discipline
FROM disciplines d 
JOIN teachers t ON t.id = d.teacher_id
WHERE t.id = 2--Id преподавтеля(Если убрать строку- все преподаватели с предметами)
GROUP by t.fullname, d.name;