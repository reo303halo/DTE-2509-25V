
````markdown
# SQL Queries for Students and Courses

## 📋 1. List All Students with Their Enrolled Courses

```sql
SELECT s.name, c.title, e.enrolled_on
FROM enrollments e
JOIN students s ON e.student_id = s.student_id
JOIN courses c ON e.course_id = c.course_id;
````

---

## 🎯 2. Find All Students Enrolled in “Database Systems”

```sql
SELECT s.name, s.email
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
JOIN courses c ON e.course_id = c.course_id
WHERE c.title = 'Database Systems';
```

---

## 🔢 3. Count How Many Students Are Enrolled in Each Course

```sql
SELECT c.title, COUNT(e.student_id) AS num_students
FROM courses c
LEFT JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id;
```

---

## 🔄 JOIN Types Explained

### INNER JOIN (Same as `JOIN` Alone)

* Returns rows only when there is a match in both tables.
* If there is no match, that row is excluded.

```sql
SELECT *
FROM students s
INNER JOIN enrollments e ON s.student_id = e.student_id;
```

### LEFT JOIN (Also Called LEFT OUTER JOIN)

* Returns all rows from the left table, and matching rows from the right.
* If there is no match, returns `NULL` for right table columns.

```sql
SELECT *
FROM students s
LEFT JOIN enrollments e ON s.student_id = e.student_id;
```

---

## Practical Queries

### 1. List Each Student's Name and the Titles of Courses They Are Enrolled In

```sql
SELECT s.name AS student_name, c.title AS course_title
FROM enrollments e
JOIN students s ON e.student_id = s.student_id
JOIN courses c ON e.course_id = c.course_id;
```

---

### 2. List All Students, Including Those Not Enrolled in Any Course

> Uses `LEFT JOIN`

```sql
SELECT s.name AS student_name, c.title AS course_title
FROM students s
LEFT JOIN enrollments e ON s.student_id = e.student_id
LEFT JOIN courses c ON e.course_id = c.course_id;
```

---

### 3. Show All Courses with the Number of Students Enrolled

```sql
SELECT c.title AS course_title, COUNT(e.student_id) AS student_count
FROM courses c
LEFT JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id;
```

---

### 4. List Students Who Are Enrolled in More Than One Course

```sql
SELECT s.name, COUNT(e.course_id) AS courses_enrolled
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
GROUP BY s.student_id
HAVING COUNT(e.course_id) > 1;
```

---

### 5. List Students Who Are **Not** Enrolled in Any Course

> Uses `LEFT JOIN` and `WHERE ... IS NULL`

```sql
SELECT s.name
FROM students s
LEFT JOIN enrollments e ON s.student_id = e.student_id
WHERE e.course_id IS NULL;
```

---

### 6. List Course Titles and the Names of the Students Enrolled, Ordered by Course

```sql
SELECT c.title AS course_title, s.name AS student_name
FROM enrollments e
JOIN courses c ON e.course_id = c.course_id
JOIN students s ON e.student_id = s.student_id
ORDER BY c.title, s.name;
```


