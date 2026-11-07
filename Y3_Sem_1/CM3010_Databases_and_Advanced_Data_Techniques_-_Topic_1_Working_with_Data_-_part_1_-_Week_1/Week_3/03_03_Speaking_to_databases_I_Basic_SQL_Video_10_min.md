# 03_Speaking_to_databases_I_Basic_SQL_Video_10_min

# Speaking to databases I: Basic SQL
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/CDVbO/speaking-to-databases-i-basic-sql

Database development requires speaking to database management software to build, populate, and query structured data. The primary language used for this interaction is Structured Query Language (SQL), which is implemented by various database packages. While MySQL is used in the labs, alternatives like PostgreSQL and SQLite offer similar commands and syntax. These implementations, however, may require consulting documentation for specific dialect differences.

The theory of relational databases distinguishes between structure manipulation and data interaction. Data Definition Language (DDL) handles the structure of the database, using commands such as `CREATE`, `DROP`, `TRUNCATE`, and `ALTER`. Data Manipulation Language (DML) focuses on the data within those structures, including commands like `SELECT`, `INSERT`, `UPDATE`, and `DELETE`.

The `SELECT` command is used to retrieve specific information from tables. It introduces a query, and subsequently, the column specification names the desired fields that will appear in the results. The syntax is generally: `SELECT column_name FROM table_name WHERE condition`.

This query structure retrieves data for all entries in the specified table, allowing constraints to filter the results. For example, to find planet names where day length exceeds 200 hours, one uses `SELECT PlanetName FROM Planets WHERE DayLength > 200`. Note that field names must be explicitly listed separate from the constraints used for filtering.

The `CREATE` command, a DDL function, is used to build new structures, specifically tables. The syntax begins with `CREATE TABLE table_name` and requires fields and columns to be defined immediately afterward in brackets.

Each column must be assigned a data type, which dictates the kind of information it holds. Textual data types are designated using `CHAR(n)`, where 'n' specifies the maximum character length. Numerical data types, such as integers, are specified as `INT` for whole numbers.

A crucial concept for defining proper structure is the Primary Key. A primary key enforces a constraint in the relational model, ensuring that every row in a table is unique. This constraint is specified by designating a unique field or combination of fields.

This mechanism ensures that the table maintains both the integrity of a table and the uniqueness required of a relation. The fundamental process involves designing the database, using SQL to manipulate its definitions and data, and enforcing rules like uniqueness and data types.

