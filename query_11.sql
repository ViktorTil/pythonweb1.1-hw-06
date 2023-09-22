--Середній бал, який певний викладач ставить певному студентові.
SELECT s.fullname AS student, t.fullname AS teacher, d.name AS discipline, ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
JOIN disciplines d ON d.id = g.discipline_id
JOIN teachers t ON t.id = d.teacher_id 
JOIN students s ON s.id = g.student_id
WHERE s.id = 24 AND t.id = 2 -- Id студента и Id преподавателя
GROUP by d.name;
