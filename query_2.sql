--Знайти студента із найвищим середнім балом з певного предмета.
SELECT d.name AS Discipline, s.fullname AS Student, ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
JOIN students s ON s.id = g.student_id
JOIN disciplines d ON d.id = g.discipline_id
WHERE d.id = 4--Id предмета
GROUP by s.fullname
ORDER by average_grade DESC
LIMIT 1;