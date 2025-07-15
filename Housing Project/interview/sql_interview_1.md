```sql
SELECT title, author, average_rating
FROM books 
WHERE average_rating
BETWEEN 3.5 AND 4.5;

SELECT DISTINCT author
FROM books;
```

```sql
SELECT id, 
  CASE
    WHEN home_points > away_points 
      THEN 'HOME WIN'
    ELSE 'AWAY WIN'
  END
FROM nba_matches;
```

```sql
SELECT genre, COUNT(id)
FROM apps
GROUP BY genre;

SELECT genre, SUM(reviews) 
FROM apps
GROUP BY genre
HAVING SUM(reviews) > 30000000;
```

```sql
SELECT name, genre, rating
FROM apps
ORDER BY rating DESC
LIMIT 20;
```

```sql
SELECT MIN(rating)
FROM apps;

SELECT MAX(rating)
FROM apps;

SELECT ROUND(AVG(rating), 2) AS 'average rating'
FROM apps;

```

```sql
SELECT *
FROM projects
JOIN employees
  ON projects.employee_id = employees.id;

SELECT *
FROM projects
LEFT JOIN employees
  ON projects.employee_id = employees.id;
```

```sql
SELECT *
FROM math_students
WHERE student_id IN (
  SELECT student_id
  FROM english_students
);

SELECT *
FROM math_students
WHERE grade IN (
  SELECT grade
  FROM math_students
  WHERE student_id = 7
);
```


```sql
SELECT *
FROM english_students
WHERE student_id
NOT IN (
  SELECT student_id
  FROM math_students
);

SELECT grade
FROM math_students
WHERE EXISTS (
  SELECT grade
  FROM english_students
);

```

```sql
SELECT title, week, gross, 
  SUM(gross) OVER (
    PARTITION BY title 
    ORDER BY week
  ) AS 'running_total_gross'
FROM box_office;
```

```sql
SELECT ROW_NUMBER()
OVER (
  ORDER BY gross
) AS 'row_num', title, week, gross
FROM box_office;
```

```sql
SELECT id, product_id, price * quantity
FROM orders;
```

```sql
SELECT date, (CAST(high AS 'REAL') + 
  CAST(low AS 'REAL')) / 2.0 AS 'average'
FROM weather;
```

```sql
SELECT purchase_id, DATE(purchase_date, '+7 days')
FROM purchases;

SELECT STRFTIME('%H', purchase_date) FROM purchases;
```
```sql
SELECT STRFTIME('%m-%d', purchase_date) AS 'reformatted'
FROM purchases;
```

