#### What is a database?
A database is an organized collection of data stored electronically, designed to efficiently manage, retrieve, and manipulate information.

#### What is a relational database?
A relational database organizes data into tables (relations) with rows and columns, where tables can be linked through relationships using keys.

#### What is an RDBMS?
RDBMS stands for Relational Database Management System, software that manages relational databases (e.g., MySQL, PostgreSQL, Oracle) and supports SQL for querying.

#### What is a table? What are a row and column within a table?
Table: A structured set of data organized in rows and columns.

Row: A single record or entry in the table.

Column: A field or attribute representing a data category in the table.

#### What is a data type?
A data type defines the kind of data a column can hold, such as integer, varchar (text), date, boolean, etc.

#### What is a primary key and a foreign key?
Primary Key: A unique identifier for each record in a table.

Foreign Key: A column that creates a link between two tables by referring to the primary key of another table.

#### What is the difference between ALTER and UPDATE?
ALTER: Changes the structure of a table (e.g., add/drop columns).

UPDATE: Modifies the data within existing rows in a table.

#### What is a query and what is a subquery?
Query: A request to retrieve or manipulate data from a database.

Subquery: A query nested inside another query, used to perform intermediate steps.

#### What are constraints?
Rules applied to table columns to enforce data integrity, such as NOT NULL, UNIQUE, CHECK, PRIMARY KEY, and FOREIGN KEY.

#### What is a statement?
A command executed in the database, such as SQL statements for querying, inserting, updating, or deleting data.

#### How do you check if a field has a value or not?
Using IS NULL to check if a field has no value, or IS NOT NULL to check if it contains a value.

#### What is the difference between DISTINCT and UNIQUE?
DISTINCT: Used in SQL queries to return only unique rows in the result set.

UNIQUE: A constraint applied on a column to prevent duplicate values in the table.

#### What is a join?
An operation that combines rows from two or more tables based on related columns.

#### What is the purpose of window functions?
They perform calculations across a set of table rows related to the current row without collapsing the result, enabling running totals, rankings, moving averages, etc.

#### What is the difference between an INNER JOIN and LEFT JOIN?
INNER JOIN: Returns rows that have matching values in both tables.

LEFT JOIN: Returns all rows from the left table and matched rows from the right table; if no match, right side returns NULL.

#### What are indexes and why are they needed?
Indexes are data structures that improve the speed of data retrieval on database tables, similar to an index in a book, reducing the need to scan the entire table.
