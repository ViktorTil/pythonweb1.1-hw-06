--Знайти середній бал, який ставить певний викладач зі своїх предметів.
SELECT t.fullname AS Teacher, d.name AS Discipline, ROUND(AVG(g.grade), 2) AS average_grade
FROM disciplines d
JOIN grades g ON g.discipline_id = d.id
JOIN teachers t ON t.id = d.teacher_id
WHERE t.id = 2 -- Id преподавателя
GROUP by t.fullname, d.name;