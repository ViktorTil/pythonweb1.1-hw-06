--Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
SELECT s.fullname AS Student, ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
LEFT JOIN students s ON s.id = g.student_id
GROUP by s.fullname
ORDER by average_grade DESC
LIMIT 5;
