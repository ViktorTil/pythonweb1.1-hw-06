--Список курсів, які певному студенту читає певний викладач.
SELECT s.fullname AS student, t.fullname AS teacher, d.name AS discipline
FROM grades g
JOIN disciplines d ON d.id = g.discipline_id
JOIN teachers t ON t.id = d.teacher_id 
JOIN students s ON s.id = g.student_id
WHERE s.id = 20 AND t.id = 2 -- Id студента и Id преподавателя
GROUP by d.name;
