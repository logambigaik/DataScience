# Common SQL Interview Questions and Answers

## 1. What is SQL?
SQL (Structured Query Language) is a programming language used to communicate with data stored in a relational database. It allows for querying, updating, and managing data using an English-like syntax.

---

## 2. What is a database?
A database is a structured collection of data stored electronically, allowing efficient access, management, and updating.

---

## 3. What is a relational database?
A relational database organizes data into tables, enabling easy identification and access based on relationships among the data using keys.

---

## 4. What is a RDBMS?
A Relational Database Management System (RDBMS) is software used to manage relational databases. It supports SQL to perform tasks like querying and updating the database. Examples: MySQL, PostgreSQL, Oracle, SQL Server.

---

## 5. What is a table?
A table is a collection of related data stored in rows and columns, like a spreadsheet.

---

## 6. What is a row and column in a table?
- **Row**: A single record in a table.
- **Column**: A field with a specific data type that holds values across all rows.

---

## 7. What is a data type?
A data type defines the kind of data a column can store, e.g., `INTEGER`, `TEXT`, `DATE`, `REAL`.

---

## 8. What is a primary key and a foreign key?
- **Primary Key**: A column or set of columns that uniquely identify each row. It must be unique and not null.
- **Foreign Key**: A column in one table that refers to the primary key in another table, establishing a relationship.

---

## 9. What is the difference between ALTER and UPDATE?
- **ALTER**: Modifies the table structure (e.g., adding a column).
- **UPDATE**: Modifies the data in existing rows.

---

## 10. What is a query?
A query is a SQL command used to retrieve data from a database.

---

## 11. What is a subquery?
A subquery is a query nested within another SQL statement. It is executed before the outer query.

---

## 12. What are constraints?
Constraints enforce rules at the column level to maintain data integrity. Examples:
- `PRIMARY KEY`
- `UNIQUE`
- `NOT NULL`
- `DEFAULT`

---

## 13. What is a statement?
A statement is a complete SQL command such as `SELECT`, `INSERT`, `UPDATE`, `ALTER`, or `DELETE`. All statements end with a semicolon `;`.

---

## 14. How do you check if a field has or doesn’t have a value?
- Check for missing value: `WHERE col IS NULL`
- Check for existing value: `WHERE col IS NOT NULL`

---

## 15. What is the difference between DISTINCT and UNIQUE?
- **DISTINCT**: SQL keyword used in queries to return unique values from result sets.
- **UNIQUE**: A column constraint that ensures all values in the column are different.

---

## 16. What are aggregate functions used for?
Aggregate functions perform calculations on multiple values and return a single result. Examples:
- `COUNT()`
- `SUM()`
- `AVG()`
- `MAX()`
- `MIN()`
- `ROUND()`

---

## 17. What is a JOIN?
A JOIN combines rows from two or more tables based on a related column between them.

---

## 18. What is the difference between INNER JOIN and LEFT JOIN?
- **INNER JOIN**: Returns only the rows where there is a match in both tables.
- **LEFT JOIN**: Returns all rows from the left table, and matched rows from the right table; unmatched right-side values appear as NULL.

---

## 19. What is the purpose of window functions?
Window functions allow you to perform calculations across a set of table rows that are somehow related to the current row without collapsing the result set. Useful for ranking, running totals, etc.

---

## 20. What are indexes and why are they needed?
Indexes are lookup structures that speed up data retrieval operations on a database table, improving performance, especially on large datasets.

---
