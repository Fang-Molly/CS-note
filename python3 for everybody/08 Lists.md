# Chapter 8  Lists

## 8.1 A list is a sequence

* **list** : a sequence of values

   * **element or item**
      * the values can be any type, a string, a float, an integer, and another list
      * separated by commas(,)
   * create a new list: enclose the elements in square brackets([ ])
      * [10, 20, 30, 40], ['crunchy frog', 'ram bladder', 'lark vomit'], ['spam', 2.0, 5, [10, 20]]
   * **nested** : a list within another list
   * **empty list**: a list contains no elements, with empty brackets []

* **assign list values to variables**

```python
>>> cheeses = ['Cheddar', 'Edam', 'Gouda']   
>>> numbers = [17, 123]  
>>> empty = []  
>>> print(cheeses, numbers, empty)   
['Cheddar', 'Edam', 'Gouda'] [17, 123] []  
```      

## 8.2 Lists are mutable

* **access the elements of a list**

   * **bracket operator `[]`**: the expression inside the brackets specifies the index
   * the indices start at 0

```python  
>>> cheeses = ['Cheddar', 'Edam', 'Gouda']  
>>> print(cheeses[0])  
Cheddar  
``` 

* **Lists are mutable 

   * change the order of items in a list
   * reassign an item in a list

```python  
>>> numbers = [17, 123]  
>>> numbers[1] = 5  
>>> print(numbers)  
[17, 5]  

# If an index has a negative value, it counts backward from the end of the list
>>> numbers[-1]
123

# Any integer expression can be used as an index
>>> numbers[1-1]
17

# If you try to read or write an element that does not exist, you get an IndexError.
>>> numbers[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

* **`in` operator** - Is something in a list?

```python
>>> cheeses = ['Cheddar', 'Edam', 'Gouda']
>>> 'Edam' in cheeses
True  
>>> 'Brie' in cheeses
False  
>>> 'Elf' not in cheeses
True
```

* **`range()` function** - returns a list of numbers that range from zero to one less than the parameter

```python
>>> print(range(4))
range(0, 4)            # [0, 1, 2, 3]

>>> friends = ['Joseph', 'Glenn', 'Sally']
>>> print(len(friends))
3
>>> print(range(len(friends)))
range(0, 3)            # [0, 1, 2]     
```

## 8.3 Traversing a list

* **`for` loop** : traverse the elements of a list

```python
>>> friends = ['Joseph', 'Glenn', 'Sally']
>>> for friend in friends :
...     print('Happy New Year:',  friend)
... 
Happy New Year: Joseph
Happy New Year: Glenn
Happy New Year: Sally

>>> friends = ['Joseph', 'Glenn', 'Sally']
>>> for i in range(len(friends)) :
...     friend = friends[i]
...     print('Happy New Year:', friend)
... 
Happy New Year: Joseph
Happy New Year: Glenn
Happy New Year: Sally
```

```python
>>> numbers = [1, 2]
>>> for i in range(len(numbers)):
...     numbers[i] = numbers[i] * 2
... 
>>> print(numbers)
[2, 4]
>>> 
>>> numbers = [1,2]
>>> numbers * 2
[1, 2, 1, 2]
```

```python
for x in empty:
    print('This never happens.')
```

## 8.4 List operations

* **Concatenating lists using the `+` operator **

```python
>>> a = [1, 2, 3]
>>> b = [4, 5, 6]
>>> c = a + b
>>> print(c)
[1, 2, 3, 4, 5, 6]
```
* **Repeating a list a given number of times using the `*` operator**

```python
>>> [1, 2, 3] * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
```

## 8.5 List slices

* **slice operator**

```python
>>> t = ['a', 'b', 'c', 'd', 'e', 'f'] 
>>> t[1:3]
['b', 'c']
>>> t[:4]
['a', 'b', 'c', 'd']
>>> t[3:]
['d', 'e', 'f']
>>> t[:]
['a', 'b', 'c', 'd', 'e', 'f'] 
```

* **reassign elements**
   
```python
>>> t = ['a', 'b', 'c', 'd', 'e', 'f'] 
>>> t[1:3] = ['x', 'y']
>>> print(t)
['a', 'x', 'y', 'd', 'e', 'f']
```

## 8.6 List methods

```python
>>> x = list()
>>> type(x)
<class 'list'>
>>> dir(x)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> 
```

* **`list.append()` method : add a new element to the end of a list**

```python
>>> stuff = list()         # create an empty list
>>> stuff.append('book')   # add elements
>>> stuff.append(99)       
>>> print(stuff)
['book', 99]
>>> stuff.append('cookie') # list stays in order and add new elements at the end
>>> print(stuff)
['book', 99, 'cookie']
```

* **`list.extend()` method : take a list as an argument and append all of the elements**

```python
>>> t1 = ['a', 'b', 'c']
>>> t2 = ['d', 'e']
>>> t1.extend(t2)
>>> print(t1)
['a', 'b', 'c', 'd', 'e']
```

* **`list.sort()` method : arrange the elements of the list from low to high**

```python
# list.sort()
>>> t = ['d', 'c', 'e', 'b', 'a']
>>> t.sort()
>>> print(t)
['a', 'b', 'c', 'd', 'e']

>>> t = ['d', 'c', 'e', 'b', 'a']
>>> print(t.sort())
None
>>> type(t.list())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'list'

# sorted(list)
>>> t = ['d', 'c', 'e', 'b', 'a']
>>> sorted(t)
['a', 'b', 'c', 'd', 'e']

>>> print(sorted(t))
['a', 'b', 'c', 'd', 'e']
>>> type(sorted(t))
<class 'list'>
```

## 8.7 Deleting elements

* **`list.pop()` method**
      
```python
>>> t = ['a', 'b', 'c']
>>> x = t.pop(1)
>>> print(t)
['a', 'c']
>>> print(x)
b

# if you don't provide an index, it deletes and returns the last element
>>> t = ['a', 'b', 'c']
>>> x = t.pop()
>>> print(t)
['a', 'b']
>>> print(x)
c
```

* **`del()` method : if you know the index and you don't need the removed value**

```python
>>> t = ['a', 'b', 'c']
>>> del t[1]
>>> print(t)
['a', 'c']
>>>
>>> t = ['a', 'b', 'c', 'd', 'e', 'f']
>>> del t[1:5]
>>> print(t)
['a', 'f']
```   

* **`list.remove()` method : if you know the element you want to remove (but not the index)**

```
>>> t = ['a', 'b', 'c']
>>> t.remove('b')
>>> print(t)
['a', 'c']
```

## 8.8 Lists and functions

* **Built-in functions**

```python
>>> nums = [3, 41, 12, 9, 74, 15]
>>> print(len(nums))
6
>>> print(max(nums))
74
>>> print(min(nums))
3
>>> print(sum(nums))
154
>>> print(sum(nums)/len(nums))
25.666666666666668
```

* **compute the average of a list of numbers entered by the user**

```python
total = 0  
count = 0   
while True:  
    inp = input('Enter a number: ')   
    if inp == 'done': break  
    value = float(inp)  
    total = total + value  
    count = count + 1   
    
average = total / count  
print('Average:', average)  
```

```python
numlist = list()   
while True:  
    inp = input('Enter a number: ')   
    if inp == 'done': break  
    value = float(inp)  
    numlist.append(value)  
    
average = sum(numlist) / len(numlist)  
print('Average:', average)
```

## 8.9 Lists and strings

* **`list()` : built-in function, convert from a string to a list of characters**
   
   * break a string into individual letters

```python
>>> s = 'spam'
>>> t = list(s)
>>> print(t)
['s', 'p', 'a', 'm']
```

* **`string.split()` : break a string into parts and produces a list of strings.**

```python
>>> abc = 'with three words'
>>> stuff = abc.split()
>>> print(stuff)
['with', 'three', 'words']
>>> print(len(stuff))
3
>>> print(stuff[0])
with
>>> for w in stuff:       # for loop
...     print(w)
... 
with
three
words
```

* **`string.split(delimiter)`: specifies which characters to use as word boundaries.**

```python
>>> s = 'spam-spam-spam'
>>> delimiter = '-'
>>> s.split(delimiter)
['spam', 'spam', 'spam']
>>> s.split('-')
['spam', 'spam', 'spam']
```

```python
# When you do not specify a delimiter, multiple spaces are treated like one delimiter
>>> line = 'A lot            of spaces'
>>> etc = line.split()
>>> print(etc)
['A', 'lot', 'of', 'spaces']
>>> etc = line.split(' ')
>>> print(etc)
['A', 'lot', '', '', '', '', '', '', '', '', '', '', '', 'of', 'spaces']
>>> 
>>> line = 'first;second;third'
>>> thing = line.split()
>>> print(thing)
['first;second;third']
>>> print(len(thing))
1
>>> thing = line.split(';')
>>> print(thing)
['first', 'second', 'third']
>>> print(len(thing))
3
```

* **`join()` : take a list of strings and concatenate the elements. **

```python
>>> t = ['pining', 'for', 'the', 'fjords']
>>> delimiter = ' '
>>> delimiter.join(t)
'pining for the fjords'
```

## 8.10 Parsing lines

From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008  

```python
fhand = open('mbox-short.txt')   
for line in fhand:
    line = line.rstrip()   
    if not line.startswith('From ') : continue   
    words = line.split()   
    print(words[2])   

Sat 
Fri 
Fri 
Fri 
...
```

```python
>>> line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
>>> words = line.split()
>>> print(words)
['From', 'stephen.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008']
>>> email = words[1]
>>> print(email)
stephen.marquard@uct.ac.za
>>> pieces = email.split('@')
>>> print(pieces)
['stephen.marquard', 'uct.ac.za']
>>> print(pieces[1])
uct.ac.za
```

## 8.11 Objects and values

```python
# two strings refer to the same object
>>> a = 'banana'
>>> b = 'banana'
>>> a is b
True

# two lists are equivalent, but not identical, not the same object
>>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>> a is b
False
```

## 8.12 Aliasing

* **reference**: the association of a variable with an object  
* **aliased**: an object with more than one reference has more than one name

```python
>>> a = [1, 2, 3]
>>> b = a
>>> b is a
True
>>> b[0] = 17
>>> print(a)
[17, 2, 3]
```

## 8.13 List arguments

```python
>>> def delete_head(t):
...     del t[0]
... 
>>> letters = ['a', 'b', 'c']
>>> delete_head(letters)
>>> print(letters)
['b', 'c']
```

```python
>>> t1 = [1, 2]
>>> t2 = t1.append(3)
>>> print(t1)
[1, 2, 3]
>>> print(t2)
None
```

```python
>>> t1 = [1, 2]
>>> t3 = t1 + [3]
>>> print(t3)
[1, 2, 3]
>>> t2 is t3
False
```

```python
>>> def tail(t):
...     return t[1:]
... 
>>> letters = [1, 2, 3, 4]
>>> tail(letters)
[2, 3, 4]
```

## 8.14 Debugging

* Don't forget that most list methods modify the argument and return None.

   * If you are used to writing string code like this: word = word.strip()
   * It is tempting to write list code like this: t = t.sort() # WRONG!

* Pick an idiom and stick with it

   * t.append(x)  # right 
   * t = t + [x]  # right 
   
   * t.append([x])  # wrong  
   * t = t.append(x)  # wrong   
   * t + [x]  # wrong   
   * t = t + x  # wrong   
   
* Make copies to avoid aliasing

   * orig = t[:]
   * t.sort()

* Lists, split, and files




## 8.15 Glossary

* **aliasing** A circumstance where two or more variables refer to the same object. 

* **delimiter** A character or string used to indicate where a string should be split. 

* **element** One of the values in a list (or other sequence); also called items. 

* **equivalent** Having the same value.

* **index** An integer value that indicates an element in a list. 

* **identical** Being the same object (which implies equivalence). 

* **list** A sequence of values.

* **list traversal** The sequential accessing of each element in a list. 

* **nested list** A list that is an element of another list.

* **object** Something a variable can refer to. An object has a type and a value. 

* **reference** The association between a variable and its value.


## 8.16 Exercises

**Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.**

```python
def chop(list):
    del list[0]
    del list[-1]

def middle(list):
    new_list = list[1:]
    del new_list[-1]
    return new_list

list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]

print(chop(list1))
print(middle(list2))

$ python3 ex_08_01.py
None
[2, 3]
```

**Exercise 2: Figure out which line of the above program is still not properly guarded. See if you can construct a text file which causes the program to fail and then modify the program so that the line is properly guarded and test it to make sure it handles your new text file.**

```python
fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()

    if len(words) < 3:
        continue
    if words[0] != 'From':
        continue
    print(words[2])
```


**Exercise 3: Rewrite the guardian code in the above example without two if statements. Instead, use a compound logical expression using the or logical operator with a single if statement.**

```python
fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[2])
```

**Exercise 4: Download a copy of the file www.py4e.com/code3/romeo.txt. Write a program to open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split function. For each word, check to see if the word is already in a list. If the word is not in the list, add it to the list. When the program completes, sort and print the resulting words in alphabetical order.**   

Enter file: romeo.txt  
['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window','with', 'yonder']  

```python
list = []
fhand = open ('romeo.txt')

for line in fhand:
    words = line.split()     # split line into words
    for word in words:
        if word in list:
            continue         # discard duplicates
        list.append(word)    # update the list
        
print(sorted(list))          # alphabetical order
```

**Exercise 5: Write a program to read through the mail box data and when you find line that starts with “From”, you will split the line into words using the split function. We are interested in who sent the message, which is the second word on the From line.**  

From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008  

You will parse the From line and print out the second word for each From line, then you will also count the number of From (not From:) lines and print out a count at the end. This is a good sample output with a few lines removed:  

python fromcount.py  
Enter a file name: mbox-short.txt   
stephen.marquard@uct.ac.za   
louis@media.berkeley.edu   
zqian@umich.edu  

[...some output removed...]  

ray@media.berkeley.edu   
cwen@iupui.edu   
cwen@iupui.edu   
cwen@iupui.edu  
There were 27 lines in the file with From as the first word  

```python
fname = input('Enter a file name: ')
fhand = open(fname)
count = 0

for line in fhand:
    line = line.rstrip()
    words = line.split()
    
    if len(words) < 3 or words[0] != 'From':
        continue
        
    email = words[1]
    print(email)
    count = count + 1

print('There were', count, 'lines in the file with From as the first word')
```

**Exercise 6: Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at the end when the user enters “done”. Write the program to store the numbers the user enters in a list and use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.**  

Enter a number: 6   
Enter a number: 2   
Enter a number: 9   
Enter a number: 3   
Enter a number: 5   
Enter a number: done   
Maximum: 9.0   
Minimum: 2.0  

```python
list = []

while True:
    num = input('Enter a number: ')
    if num == 'done':
        break
    try:
        value = float(num)
    except:
        print('Invalid input')
        quit()

    list.append(value)

print('Maximum:', max(list))
print('Minimum:', min(list))
```
