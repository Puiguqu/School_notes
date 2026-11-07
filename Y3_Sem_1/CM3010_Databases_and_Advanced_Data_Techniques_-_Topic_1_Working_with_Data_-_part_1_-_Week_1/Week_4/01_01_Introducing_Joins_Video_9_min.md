# 01_Introducing_Joins_Video_9_min

# Introducing Joins
Video • 9 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/FAMiP/introducing-joins

Database joins are essential mechanisms used in relational databases to combine data from multiple tables, allowing queries to access relationships between entities. The concept of a join arises when querying requires linking tables, such as relating planets and their associated moons. There are three primary types of joins discussed: the Cross Join, the Inner Join, and the Outer Join.

The Cross Join is the simplest type, accomplished by listing multiple tables directly in the `FROM` clause of a SQL statement. Its defining characteristic is that it combines every single row from one table with every single row from every other table. For example, if one table has seven records and another has twelve, a Cross Join results in $7 \times 12 = 84$ rows.

A significant technical caution must be applied to Cross Joins because they quickly produce extremely large and often meaningless result sets, such as pairing every planet with every moon regardless of association. Operations like sorting or filtering on these massive tables consume substantial memory or disk resources.

The Inner Join is the most commonly used and constrained join type, focusing only on matches between tables. While an inner join can sometimes be implicitly recognized by the Database Management System (DBMS) using an equals constraint in the `WHERE` clause (e.g., `WHERE planet.name = moon.planet`), a clearer syntax involves explicit joining.

Explicit inner join syntax is defined as `FROM table1 INNER JOIN table2 ON condition`. This method specifies the first table, the join type, the second table, and the exact criterion for combination.

This constrained approach significantly reduces the results; using the previous example of eight planets and 173 moons, a Cross Join yields 1,384 meaningless results, whereas an Inner Join yields only the 173 meaningful, associated results.

The Outer Join, which includes Left and Right variations, preserves records even when no match exists in the other table. Unlike the Inner Join, which discards rows without a match, the Outer Join ensures all rows from one specified table are included.

Specifically, a `LEFT JOIN` (or `LEFT OUTER JOIN`) ensures that all rows from the left-hand table are displayed, regardless of whether a match exists in the right-hand table.

In cases where a row from the left table has no match in the right table, the resulting fields from the right table will contain `NULL` entries. This feature is invaluable for finding records that lack corresponding matches in related datasets.

In summary, joins fundamentally control the row count and content of a query's output. Cross Joins are expansive and must be heavily constrained. Inner Joins are precise, returning only related pairs. Outer Joins ensure data preservation, displaying all records from one side, whether matched or not.

