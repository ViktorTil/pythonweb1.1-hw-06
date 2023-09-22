--Знайти оцінки студентів у окремій групі з певного предмета.
SELECT gr.name AS Group_name, d.name AS Discipline, s.fullname AS Student, g.grade AS Grade
FROM grades g
JOIN disciplines d ON d.id = g.discipline_id
JOIN students s ON s.id = g.student_id
JOIN [groups] gr ON gr.id = s.group_id
WHERE gr.id = 1 AND d.id = 1--Id группы и Id предмета
ORDER by s.fullname;