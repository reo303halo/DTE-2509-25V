-- Drop tables if they already exist
DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS courses;

-- Create students table
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

-- Create courses table
CREATE TABLE courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    instructor VARCHAR(100)
);

-- Create enrollments table (many-to-many relationship)
CREATE TABLE enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrolled_on DATE,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Insert sample students
INSERT INTO students (name, email) VALUES
('Alice Johnson', 'alice@example.com'),
('Bob Smith', 'bob@example.com'),
('Charlie Brown', 'charlie@example.com’),
(‘Bobby ‘Brown, ‘bobby@examples.com),
(‘Sally Rabarba, ‘sally@example.com’),
;

-- Insert sample courses
INSERT INTO courses (title, instructor) VALUES
('Database Systems', ‘Werner),
('Web Development', ‘Roy’),
('Machine Learning', ‘Bernt’),
(‘Python’, ‘Frode’),
(‘Math’, ‘Arlene’);

-- Insert sample enrollments
INSERT INTO enrollments (student_id, course_id, enrolled_on) VALUES
(1, 1, '2025-01-10'),
(1, 2, '2025-01-11'),
(2, 1, '2025-01-12'),
(3, 3, '2025-01-13’),
(5, 3, '2025-01-13’),
(6, 2, '2025-01-12’),;