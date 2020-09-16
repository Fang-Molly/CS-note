# Chapter 10  Tuples

## 10.1 Tuples are immutable

* **tuple**
   * a sequence of values, much like a list
   * the values can be any type
   * tuple can't be used as a variable name.
   * be indexed by integers
   * be immutable
   * be comparable and hashable
      * can sort lists of them
      * can be used as key values in Python dictionaries
      
* **syntax of tuple**
   * each element must be enclosed by ''
   * enclose tuples in parentheses to help identify tuples quickly
   
```python
>>> t = 'a', 'b', 'c', 'd', 'e'
>>> t = ('a', 'b', 'c', 'd', 'e')
```
   * have to include the final comma when a tuple has a single element; Without comma, the type is string

```python
>>> t1 = ('a',)
>>> type(t1)
<class 'tuple'>
>>> t2 = ('a')
>>> type(t2)
<class 'str'>
```

* **built-in function tuple**: another way to construct a tuple

```python
# create an empty tuple with no argument
>>> t = tuple()
>>> print(t)
()
```
```python
>>> t = tuple('lupins')
>>> print(t)
('l', 'u', 'p', 'i', 'n', 's')
```

* Most list operator also works on tuples

```python
>>> t = ('a', 'b', 'c', 'd', 'e')
>>> print(t[0])
a
>>> print(t[1:3])
('b', 'c')
```

* You can't modify the elements of a tuple, you can replace one tuple with another

```python
>>> t[0] = 'A'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment

>>> t = ('A',) + t[1:]
>>> print(t)
('A', 'b', 'c', 'd', 'e')
```

## 10.2 Comparing tuples

* The comparison operators work with tuples and other sequences. 

   * Comparing starts by the first element from each sequence. If they are equal, it goes on to the next element, and so on, until it finds elements that differ. 
   
   * Subsuquent elements are not considered, even if they are really big.

```python
>>> (0, 1, 2) < (0, 3, 4)
True
>>> (0, 1, 2000000) < (0, 3, 4)
True
```
* sort function

   * primarily by first element, if it is equal, then by second element, and so on
   
* DSU pattern

   * decorate: building a list of tuples with one or more sort keys preceding the elements from the sequence
   
   * sort: using the Python built-in sort
   
   * undecorate: by extracting the sorted elements of the sequence

```python
# suppose you have a list of words and you want to sort them from longest to shortest
>>> txt = 'but soft what light in yonder window breaks'
>>> words = txt.split()
>>> t = list()
>>> for word in words:
...     t.append((len(word), word))
... 
>>> t.sort(reverse=True)
>>> 
>>> res = list()
>>> for length, word in t:
...     res.append(word)
... 
>>> print(res)
['yonder', 'window', 'breaks', 'light', 'what', 'soft', 'but', 'in']
```

## 10.3 Tuple assignment

* have a tuple on the left side and assign more than one variable at a time in a single statement

```python
>>> m = [ 'have', 'fun' ]
>>> x, y = m
>>> x
'have'
>>> y
'fun'
>>>
# omiting the parentheses is an equally valid syntax
>>> m = [ 'have', 'fun' ] 
>>> (x, y) = m
>>> x
'have'
>>> y 'fun' >>>

```
```python
>>> m = [ 'have', 'fun' ]
>>> x = m[0]
>>> y = m[1]
>>> x
'have'
>>> y
'fun'
>>> 
```

* swap the values of two variables in a single statement
   * the left side : a tuple of variables; the right side : a tuple of expressions
   * the number of variables on the left and the number of values on the right must be same
   * the right side can be any kind of sequences: string, list or tuple
   
```python   
>>> a, b = b, a
>>> a, b = 1, 2, 3
ValueError: too many values to unpack
```
```python
>>> addr = 'monty@python.org'
>>> uname, domain = addr.split('@')
>>> print(uname)
monty
>>> print(domain)
python.org
```

## 10.4 Dictionaries and tuples

* ```items``` method : returns a list of tuples, each tuple is a key-value pair
   * the items are in no particular order
   * sort a dictionary in ascending alphabetical by the key value
   
```python
>>> d = {'a':10, 'b':1, 'c':22}
>>> t = list(d.items())
>>> print(t)
[('a', 10), ('b', 1), ('c', 22)]
>>> t.sort()
>>> t
[('a', 10), ('b', 1), ('c', 22)]
>>> 
```

## 10.5 Multiple assignment with dictionaries

* combine ```items```, tuple assignment, and ```for``` to traverse the keys and values of a dictionary in a single loop

```python
>>> d = {'a':10, 'b':1, 'c':22}
>>> for key, val in list(d.items()):
...     print(val, key)
... 
10 a
1 b
22 c
```

```python
>>> d = {'a':10, 'b':1, 'c':22}
>>> l = list()
>>> for key, val in d.items():
...     l.append((val, key))
... 
>>> l
[(10, 'a'), (1, 'b'), (22, 'c')]
>>> l.sort(reverse=True)
>>> l
[(22, 'c'), (10, 'a'), (1, 'b')]
>>> 
```

## 10.6 The most common words

```python
import string
fhand = open('remeo.txt')
counts = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:10]:
    print(key, val)

3 the
3 is
3 and
2 sun
1 yonder
1 with
1 window
1 who
1 what
1 through
```


## 10.7 Using tuples as keys in dictionaries

use a tuple as a composite key in a dictionary

directory[last,first] = number

for last, first in directory:
    print(first, last, directory[last,first])



## 10.8 Sequences: strings, lists, and tuples - Oh My!




## 10.9 Debugging




## 10.10 Glossary

* **comparable** : A type where one value can be checked to see if it is greater than, less than, or equal to another value of the same type. Types which are comparable can be put in a list and sorted.

* **data structure** : A collection of related values, often organized in lists, dictionaries, tuples, etc.

* **DSU** : Abbreviation of “decorate-sort-undecorate”, a pattern that involves building a list of tuples, sorting, and extracting part of the result.

* **gather** : The operation of assembling a variable-length argument tuple.

* **hashable** : A type that has a hash function. Immutable types like integers, floats, and strings are hashable; mutable types like lists and dictionaries are not. 

* **scatter** : The operation of treating a sequence as a list of arguments.

* **shape** : (of a data structure) A summary of the type, size, and composition of a data structure.

* **singleton** : A list (or other sequence) with a single element.

* **tuple** : An immutable sequence of elements.

* **tuple assignment** : An assignment with a sequence on the right side and a tuple of variables on the left. The right side is evaluated and then its elements are assigned to the variables on the left.

## 10.11 Exercises

Exercise 1: Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line. Count the num- ber of messages from each person using a dictionary.

After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

Enter a file name: mbox-short.txt 
cwen@iupui.edu 5

Enter a file name: mbox.txt 
zqian@umich.edu 195

Exercise 2: This program counts the distribution of the hour of the day for each of the messages. You can pull the hour from the “From” line by finding the time string and then splitting that string into parts using the colon character. Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.

python timeofday.py
Enter a file name: mbox-short.txt 
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1

Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should convert all the input to lower case and only count the letters a-z. Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.


