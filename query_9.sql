--Знайти список курсів, які відвідує студент.
SELECT s.fullname AS Student, d.name AS Discipline
FROM grades g
JOIN disciplines d ON d.id = g.discipline_id
JOIN students s ON s.id = g.student_id
WHERE s.id = 18 -- Id студента
GROUP by d.name;