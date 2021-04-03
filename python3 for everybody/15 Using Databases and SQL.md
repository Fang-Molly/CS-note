# Chapter 15 Using Databases and SQL

## 15.1 What is a database?

* **database** : a file that is organized for storing data

   * permanent storage : persist after the program ends
   * storage size : limited to the size of the memory in the computer

* database systems: Oracle, MySQL, Microsoft SQL Server, PostgreSQL, and SQLite.

## 15.2 Database concepts

tables, rows, and columns   

relation, tuple, and attribute


## 15.3 Database Browser for SQLite

http://sqlitebrowser.org/


## 15.4 Creating a database table

```python
# create a database file and a table named Tracks with two columns in
the database

import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

conn.close()
```

```python
import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)',
    ('Thunderstruck', 20))
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)',
    ('My Way', 15))
conn.commit()

print('Tracks:')
cur.execute('SELECT title, plays FROM Tracks') 
for row in cur:
  print(row)
  
cur.execute('DELETE FROM Tracks WHERE plays < 100')
conn.commit()

cur.close()

$
Tracks:
('Thunderstruck', 20)
('My Way', 15)
```

## 15.5 Structured Query Language summary

## 15.6 Spidering Twitter using a database

## 15.7 Basic data modeling

## 15.8 Programming with multiple tables

### 15.8.1 Constraints in database tables

### 15.8.2 Retrieve and / or insert a record

### 15.8.3 Storing the friend relationship

## 15.9 Three kinds of keys

## 15.10 Using JOIN to retrieve data

## 15.11 Summary

## 15.12 Debugging

## 15.13 Glossary

