# Write your MySQL query statement below
# adapted from https://leetcode.com/problems/students-with-invalid-departments/discuss/869496/NOT-IN

SELECT ID, NAME
FROM STUDENTS
WHERE DEPARTMENT_ID NOT IN ( SELECT ID FROM DEPARTMENTS )
