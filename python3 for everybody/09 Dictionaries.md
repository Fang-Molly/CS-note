# Chapter 9  Dictionaries

* **dictionaries** - Python's most powerful data collection
   * Enclosed by curly braces {}
   * Indices: can be any type, called keys 
   * Key-value pairs: each key maps to a value
   * No order - like bags
   
* **`dict()` function**
   * a built-in function, create a new dictionary with no items
   * can't be used as a variable name
   * **curly brackets `{}`**: represent an empty dictionary
   * look up the corresponding values: use square brackets `[]`
   
```python
# create an empty dictionary
>>> eng2sp = dict()
>>> print(eng2sp)
{}          

# add items using square brackets []
>>> eng2sp['one'] = 'uno'
>>> print(eng2sp)
{'one': 'uno'}

# look up the corresponding values using square brackets []
>>> eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
>>> print(eng2sp)
{'one': 'uno', 'two': 'dos', 'three': 'tres'}
>>> print(eng2sp['two'])
dos

# if the key isn't in the dictionary, you get an error
>>> print(eng2sp['four'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'four'
>>> 'four' in eng2sp
False
```

* **`len()` function** - returns the number of key-value pairs

```python
>>> eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
>>> len(eng2sp)
3
```

* **`in` operator** - see if a key is in the dictionary

```python
# in operator gets keys
>>> eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
>>> 'one' in eng2sp
True
>>> 'uno' in eng2sp
False

```

* **`values()` method** - see if a value is in the dicionary

```python
# dictionaries.values() gets values
>>> eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
>>> eng2sp.values()
dict_values(['uno', 'dos', 'tres'])
>>> 'uno' in eng2sp.values()
True
>>> vals = list(eng2sp.values())
>>> print(vals)
['uno', 'dos', 'tres']
>>> 'uno' in vals
True
```
* **Comparing lists and dictionaries**

```python
# list: [0]-21; [1]-183
>>> lst = list()
>>> lst.append(21)
>>> lst.append(183)
>>> print(lst)
[21, 183]
>>> lst[0] = 23
>>> print(lst)
[23, 183]

# dictionary: ['age']-23; ['course']-182
>>> ddd['age'] = 21
>>> ddd['course'] = 182
>>> print(ddd)
{'age': 21, 'course': 182}
>>> ddd['age'] = 23
>>> print(ddd)
{'age': 23, 'course': 182}
```

## 9.1 Dictionary as a set of counters

* **count how many times something appears**

```python
>>> word = 'brontosaurus'
>>> d = dict()
>>> for c in word:
...     if c not in d:
...         d[c] = 1
...     else:
...         d[c] = d[c] + 1
... 
>>> print(d)
{'b': 1, 'r': 2, 'o': 2, 'n': 1, 't': 1, 's': 2, 'a': 1, 'u': 2}
```

```python
>>> counts = dict()
>>> names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
>>> for name in names:
...     if name not in counts:
...             counts[name] = 1
...     else:
...             counts[name] = counts[name] + 1
... 
>>> print(counts)
{'csev': 2, 'cwen': 2, 'zqian': 1}
```

* **`dictionary.get()` method : take a key and a default value**

```python
>>> counts = {'chuck' : 1, 'annie' : 42, 'jan' : 100}

# if the key appears in the dictionary, returns the corresponding value
>>> print(counts.get('jan', 0))
100

# if the key doesn't appear in the dictionary, returns the default value and no traceback
>>> print(counts.get('trim', 0))
0
```

* **Simplified counting with `get()`**

```python
>>> word = 'brontosaurus'
>>> d = dict()
>>> for c in word:
...     d[c] = d.get(c,0) + 1
... 
>>> print(d)
{'b': 1, 'r': 2, 'o': 2, 'n': 1, 't': 1, 's': 2, 'a': 1, 'u': 2}
```

```python
>>> counts = dict()
>>> names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
>>> for name in names:
...     counts[name] = counts.get(name,0) + 1
... 
>>> print(counts)
{'csev': 2, 'cwen': 2, 'zqian': 1}
```

* **Counting Pattern**

```python
counts = dict()
line = input('Enter a line of text: \n')
words = line.split()

print('Words:', words)
print('Counting...')

for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts', counts)

$ python3 counter.py
Enter a line of text:
the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car 
Words: ['the', 'clown', 'ran', 'after', 'the', 'car', 'and', 'the', 'car', 'ran', 'into', 'the', 'tent', 'and', 'the', 'tent', 'fell', 'down', 'on', 'the', 'clown', 'and', 'the', 'car']
Counting...
Counts {'the': 7, 'clown': 2, 'ran': 2, 'after': 1, 'car': 3, 'and': 3, 'into': 1, 'tent': 2, 'fell': 1, 'down': 1, 'on': 1}
```

## 9.2 Dictionaries and files

```python
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)
```
* counts[word] += 1 is equivalent to counts[word] = counts[word] + 1
   * -=, *=, /=


## 9.3 Looping and dictionaries

* **`for` statement: traverse the keys of the dictionary**

```python
>>> counts = {'chuck' : 1, 'annie' : 42, 'jan' : 100}
>>> for key in counts:
...     print(key, counts[key])
... 
chuck 1
annie 42
jan 100
```

```python
>>> counts = {'chuck' : 1, 'annie' : 42, 'jan' : 100}
>>> for key in counts:
...     if counts[key] > 10 :
...         print(key, counts[key])
... 
jan 100
annie 42
```

```python
>>> counts = {'chuck' : 1, 'annie' : 42, 'jan' : 100}
>>> lst = list(counts.keys())
>>> print(lst)
['chuck', 'annie', 'jan']
>>> lst.sort()
>>> for key in lst:
...     print(key, counts[key])
... 
annie 42
chuck 1
jan 100
```

```python
>>> counts = {'chuck' : 1, 'annie' : 42, 'jan' : 100}
>>> list(counts)
['chuck', 'annie', 'jan']
>>> counts.keys()
dict_keys(['chuck', 'annie', 'jan'])
>>> counts.values()
dict_values([1, 42, 100])
>>> counts.items()
dict_items([('chuck', 1), ('annie', 42), ('jan', 100)])
```

```python
>>> counts = {'chuck' : 1, 'annie' : 42, 'jan' : 100}
>>> for a,b in counts.items():
...     print(a,b)
... 
chuck 1
annie 42
jan 100
```

## 9.4 Advanced text parsing

* **translate method : line.translate(str.maketrans(fromstr, tostr, deletestr))**

```python
>>> import string
>>> string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
```

```
import string

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
```            

## 9.5 Debugging

Here are some suggestions for debugging large datasets:

* Scale down the input

* Check summaries and types

* Write self-checks

* Pretty print the output


## 9.6 Glossary

* **dictionary** A mapping from a set of keys to their corresponding values. 
* **hashtable** The algorithm used to implement Python dictionaries.
* **hash function** A function used by a hashtable to compute the location for a key.
* **histogram** A set of counters.
* **implementation** A way of performing a computation.
* **item** Another name for a key-value pair.
* **key** An object that appears in a dictionary as the first part of a key-value pair. 
* **key-value pair** The representation of the mapping from a key to a value. 
* **lookup** A dictionary operation that takes a key and finds the corresponding value.
* **nested loops** When there are one or more loops “inside” of another loop. The inner loop runs to completion each time the outer loop runs once.
* **value** An object that appears in a dictionary as the second part of a key-value pair. This is more specific than our previous use of the word “value”.


## 9.7 Exercises

**Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt

Write a program that reads the words in words.txt and stores them as keys in a dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.**



**Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).**

Sample Line:

From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

Sample Execution:

python dow.py
Enter a file name: mbox-short.txt 
{'Fri': 20, 'Thu': 6, 'Sat': 1}

```python
fname = input('Enter a file name: ')
try: 
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
    
days = dict()

for line in fhand:
    dayslist = line.split()
    if line.startswith('From'):
        day = line[2]
        days[day] = days.get(day,0) + 1
print(days)
```


**Exercise 3: Write a program to read through a mail log, build a his- togram using a dictionary to count how many messages have come from each email address, and print the dictionary.**

Enter file name: mbox-short.txt

{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3, 
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1, 'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3, 'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1, 
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}



**Exercise 4: Add code to the above program to figure out who has the most messages in the file. After all the data has been read and the dic- tionary has been created, look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print how many messages the person has.**

Enter a file name: mbox-short.txt 
cwen@iupui.edu 5

Enter a file name: mbox.txt 
zqian@umich.edu 195



**Exercise 5: This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.**

python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7, 
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
