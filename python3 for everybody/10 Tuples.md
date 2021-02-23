# Chapter 10  Tuples

## 10.1 What is a tuple

* **tuple**
   * a sequence of values, much like a list
   * the values can be any type
   * be indexed by integers, staring at 0
   * tuple can't be used as a variable name.
   * be immutable
   * be comparable and hashable
      * can sort lists of them
      * can be used as key values in Python dictionaries
   
```python
# comma-separated list of values, each element must be enclosed by ''
>>> t = 'a', 'b', 'c', 'd', 'e'
>>> print(t)
('a', 'b', 'c', 'd', 'e')
>>> type(t)
<class 'tuple'>

# It is common to enclose tuples in parentheses ()
>>> t = ('a', 'b', 'c', 'd', 'e')
>>> print(t)
('a', 'b', 'c', 'd', 'e')
>>> type(t)
<class 'tuple'>
```

```python
# create a tuple with a single element, you have to include the final comma
>>> m = ('a',)
>>> type(m)
<class 'tuple'>

# without the comma, the type is string
>>> m = ('a')
>>> type(m)
<class 'str'>
```

* **`tuple()`**: built-in function, to create a tuple

```python
# create an empty tuple with no argument
>>> t = tuple()
>>> print(t)
()
>>> type(t)
<class 'tuple'>

# If the argument is a sequence(string, list, or tuple), the result of the call to tuple is a tuple with the elements of the sequence:
>>> t = tuple('lupins')
>>> print(t)
('l', 'u', 'p', 'i', 'n', 's')
```

* **Most list operator also works on tuples**

```python
>>> t = ('a', 'b', 'c', 'd', 'e')
>>> print(t[0])
a
>>> print(t[1:3])
('b', 'c')

>>> y = (1, 9, 2)
>>> print(y)
(1, 9, 2)
>>> print(max(y))
9
>>> for iter in y:
...     print(iter)
... 
1
9
2
```

* **Tuples are immutable**

```python
# lists are mutable
>>> x = [9, 8, 7]
>>> x[2] = 6
>>> print(x)
[9, 8, 6]

# strings are immutable
>>> y = 'ABC'
>>> y[2] = 'D'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment

# tuples are immutable 
>>> t[0] = 'A'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
# replace one tuple with another
>>> t = ('A',) + t[1:]
>>> print(t)
('A', 'b', 'c', 'd', 'e')
```

* **Things not to do with tuples**

```python
>>> l = list()
>>> dir(l)
['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

>>> t = tuple()
>>> dir(t)
['count', 'index']
```

```python
>>> x = [3, 2, 1]
>>> x.sort()
>>> print(x)
[1, 2, 3]
>>> x.append(5)
>>> print(x)
[1, 2, 3, 5]
>>> x.reverse()
>>> print(x)
[5, 3, 2, 1]

>>> x = (3, 2, 1)
>>> x.sort()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'sort'
>>> x.append(5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'append'
>>> x.reverse()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'reverse'
```

* **Why use Tuples: more efficient**

   * Tuples are simpler and more efficient in memory use and performance than lists.

   * We prefer tuples over lists when we are making "temporary variables"
 

## 10.2 Tuples are comparable

* **Comparison operators**

   * Comparing starts by the first element from each sequence. If they are equal, it goes on to the next element, and so on, until it finds elements that differ. Subsuquent elements are not considered, even if they are really big.

```python
>>> (0, 1, 2) < (0, 3, 4)
True
>>> (0, 1, 2000000) < (0, 3, 4)
True
>>> ('Jones', 'Sally') < ('Jones','Sam')
True
```
* **Sorting lists of tuples**

   * sort the dictionary by the key using the `items()` method and `sorted()` function
   
```python
>>> d = {'a':10, 'b':1, 'c':22}
>>> d.items()
dict_items([('a', 10), ('b', 1), ('c', 22)])
>>> sorted(d.items())
[('a', 10), ('b', 1), ('c', 22)]
```

* **DSU pattern**

   * **decorate**: building a list of tuples with one or more sort keys preceding the elements from the sequence
   
   * **sort**: using the Python built-in sort
   
   * **undecorate**: by extracting the sorted elements of the sequence

```python
# suppose you have a list of words and you want to sort them from longest to shortest
txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))

t.sort(reverse=True)

res = list()
for length, word in t:
    res.append(word)

print(res)

$ python3 tuple.sort.py
['yonder', 'window', 'breaks', 'light', 'what', 'soft', 'but', 'in']
```

## 10.3 Tuples and assignment

* We can have a tuple on the left side and assign more than one variable at a time in a single statement

```python
>>> (x, y) = (4, 'fred')
>>> print(y)
fred

# omiting the parentheses is an equally valid syntax
>>> x, y = 4, 'fred'
>>> print(y)
fred
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
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: too many values to unpack (expected 2)
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

* **`items()` method** : returns a list of tuples, each tuple is a key-value pair
   * the items are in no particular order
   * sort a dictionary in ascending alphabetical by the key value
   
```python
>>> d = {'a':10, 'b':1, 'c':22}
>>> t = d.items()
>>> print(t)
dict_items([('a', 10), ('b', 1), ('c', 22)])
>>> l = list(t)
>>> print(l)
[('a', 10), ('b', 1), ('c', 22)]
>>> l.sort()
>>> l
[('a', 10), ('b', 1), ('c', 22)]
>>> 
```

## 10.5 Multiple assignment with dictionaries

* combine `items`, tuple assignment, and `for` to traverse the keys and values of a dictionary in a single loop

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
>>> l.sort(reverse=True)    # or l = sorted(l, reverse=True)
>>> l
[(22, 'c'), (10, 'a'), (1, 'b')]  
>>> 
```

* Shorter version

```python
>>> d = {'a':10, 'b':1, 'c':22}
>>> print(sorted([(v,k) for k,v in d.items()]))
[(1, 'b'), (10, 'a'), (22, 'c')]
```

## 10.6 The most common words

* The top 10 most common words

```python
import string
fhand = open('remeo.txt')
counts = dict()

for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:10]:
    print(key, val)

$ pyhton3 common_words.py
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

* use a tuple as a composite key in a dictionary, because tuples are hashable and lists are not

```python
# create a telephone directory that maps from last-name, first-name pairs to telephone numbers

directory[last,first] = number

for last, first in directory:
    print(first, last, directory[last,first])
```

--------------------------

## Glossary

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

-------------------------

## Exercises

Exercise 1: Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.

After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

Enter a file name: mbox-short.txt 
cwen@iupui.edu 5

Enter a file name: mbox.txt 
zqian@umich.edu 195


```python
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        counts[words[1]] = counts.get(words[1], 0) + 1

lst = list()
for email, count in list(counts.items()):
    lst.append((count, email))

lst.sort(reverse=True)
# print(lst)

for count, email in lst[:1]:
    print(email, count)
```


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

```python
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        time = words[5]
        hour = time.split(':')
        counts[hour[0]] = counts.get(hour[0], 0) + 1

lst = list()
for hour, count in list(counts.items()):
    lst.append((hour, count))

lst.sort()

for hour, count in lst[:]:
    print(hour, count)
```


Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should convert all the input to lower case and only count the letters a-z. Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.

```python
import string

fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = 0
counts = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        for letter in word:
            counts[letter] = counts.get(letter, 0) + 1

lst = list()
for letter, count in list(counts.items()):
    lst.append((count, letter))
    lst.sort(reverse=True)
for count, letter in lst:
    print(letter, count)
```
