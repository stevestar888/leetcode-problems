-- https://leetcode.com/problems/combine-two-tables/

SELECT person.firstName, person.lastName, address.city, address.state 
FROM person
left join address on person.personId = address.personId