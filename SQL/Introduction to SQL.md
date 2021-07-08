Introduction to SQL
===================

# 1. Selecting columns

## 1.1 Onboarding - Tables

## 1.2 Onboarding - Query Result

```
SELECT name FROM people
```

## 1.3 Onboarding - Errors

## 1.4 Onboarding - Multi-step Exercises

```
SELECT 'SQL'
AS result
```

## 1.5 Beginning your SQL journey

* SQL - Structured Query Language

    * a language for interacting with data stored in something called a relational database

* row/record

* column/field

## 1.6 SELECTing single columns

* `SELECT` statement
    * no case-sensitive

```
SELECT name
FROM people;
```

## 1.7 SELECTing multiple columns

```
SELECT name, birthdate
FROM people;
```

* select all columns from a table

```
SELECT *
FROM people;
```

* limit the number of rows returned

```
SELECT *
FROM people
LIMIT 10;
```

## 1.8 SELECT DISTINCT

* select all the unique values from a column

```
SELECT DISTINCT language
FROM films;
```

## 1.9 Learning to COUNT

* COUNT() function - return the number of rows in one or more columns

```
SELECT COUNT(*)
FROM people;
```

## 1.10 Practice with COUNT

* count the number of non-missing values in a particular column

```
SELECT COUNT(birthdate)
FROM people;
```

* combine COUNT() with DISTINCT() to count the number of distinct values in a column

```
SELECT COUNT(DISTINCT birthdate)
FROM people;
```

# 2. Selecting columns

## 2.1 Filtering results

















