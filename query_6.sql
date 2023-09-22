--Знайти список студентів у певній групі.
SELECT gr.name AS Group_name, s.fullname AS Student
FROM [groups] gr
JOIN students s ON s.group_id = gr.id
WHERE gr.id = 1 -- Id группы
ORDER by s.fullname;