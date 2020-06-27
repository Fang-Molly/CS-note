# Chapter 8  Lists

## 8.1 A list is a sequence

* **list** : a sequence of values
   * element or item : the values can be any type, a string, a float, an integer, and anther list
   * enclose the elements in square brackets([ ])
      * [10, 20, 30, 40], ['crunchy frog', 'ram bladder', 'lark vomit'], ['spam', 2.0, 5, [10, 20]]
   * nested : a list within another list
   * empty list: a list contains no elements, with empty brackets []

* assign list values to variables

```python
>>> cheeses = ['Cheddar', 'Edam', 'Gouda'] 
>>> numbers = [17, 123]
>>> empty = []
>>> print(cheeses, numbers, empty) 
['Cheddar', 'Edam', 'Gouda'] [17, 123] []
```      

## 8.2 Lists are mutable

* **access the elements of a list**
   * bracket operator[]: the expression inside the brackets specifies the index
   * the index of a list start at 0

```python
>>> cheeses = ['Cheddar', 'Edam', 'Gouda']
>>> print(cheeses[0])
Cheddar
```

* Lists are mutable because you can change the order of items in a list or reassign an item in a list.

* reassign an item in a list

```python
>>> numbers = [17, 123]
>>> numbers[1] = 5
>>> print(numbers)
[17, 5]
```

* **in operator**

```python
>>> cheeses = ['Cheddar', 'Edam', 'Gouda']
>>> 'Edam' in cheeses
True
>>> 'Brie' in cheeses
False
```

## 8.3 Traversing a list

* **for loop** : read the elements of the list

```python
>>> cheeses = ['Cheddar', 'Edam', 'Gouda']
>>> for cheese in cheeses:
...     print(cheese)
... 
Cheddar
Edam
Gouda
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

* **the + operator concatenates lists**

```python
>>> a = [1, 2, 3]
>>> b = [4, 5, 6]
>>> c = a + b
>>> print(c)
[1, 2, 3, 4, 5, 6]
```
* **the * operator repeats a list a given number of times**

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

* **update elements**
   
```python
>>> t = ['a', 'b', 'c', 'd', 'e', 'f'] 
>>> t[1:3] = ['x', 'y']
>>> print(t)
['a', 'x', 'y', 'd', 'e', 'f']
```

## 8.6 List methods

* **append() method : add a new element to the end of a list**

```python
>>> t = ['a', 'b', 'c']
>>> t.append('d')
>>> print(t)
['a', 'b', 'c', 'd']
```

* **extend() method : take a list as an argument and append all of the elements**

```
>>> t1 = ['a', 'b', 'c']
>>> t2 = ['d', 'e']
>>> t1.extend(t2)
>>> print(t1)
['a', 'b', 'c', 'd', 'e']
```

* **sort() method : arrange the elements of the list from low to high**

```
>>> t = ['d', 'c', 'e', 'b', 'a']
>>> t.sort()
>>> print(t)
['a', 'b', 'c', 'd', 'e']
```

## 8.7 Deleting elements

* **pop() method**

   * if you know the index of the element you want
      
```python
>>> t = ['a', 'b', 'c']
>>> x = t.pop(1)
>>> print(t)
['a', 'c']
>>> print(x)
b
```
   * if you don't provide an index, it deletes and returns the last element

```python
>>> t = ['a', 'b', 'c']
>>> x = t.pop()
>>> print(t)
['a', 'b']
>>> print(x)
c
```

* **del() method : if you know the index and you don't need the removed value**

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

* **remove() method : if you know the element you want to remove (but not the index)**

```
>>> t = ['a', 'b', 'c']
>>> t.remove('b')
>>> print(t)
['a', 'c']
```

## 8.8 Lists and functions

* **built-in functions**

```
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

```
total = 0 
count = 0 
while (True):
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
while (True):
    inp = input('Enter a number: ') 
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist) 
print('Average:', average)
```

## 8.9 Lists and strings

* **list() : built-in function, convert from a string to a list of characters**
   * break a string into individual letters

```python
>>> s = 'spam'
>>> t = list(s)
>>> print(t)
['s', 'p', 'a', 'm']
```

* **split() : break a string into words**

```python
>>> s = 'pining for the fjords'
>>> t = s.split()
>>> print(t)
['pining', 'for', 'the', 'fjords']
>>> print(t[2])
the
```

* **split(delimiter): specifies which characters to use as word boundaries.**

```python
>>> s = 'spam-spam-spam'
>>> delimiter = '-'
>>> s.split(delimiter)
['spam', 'spam', 'spam']
>>> s.split('-')
['spam', 'spam', 'spam']
```

* **join() : take a list of strings and concatenate the elements. **

```python
>>> t = ['pining', 'for', 'the', 'fjords']
>>> delimiter = ' '
>>> delimiter.join(t)
'pining for the fjords'
```

## 8.10 Parsing lines






# 8.11 Objects and values





# 8.12 Aliasing

# 8.13 List arguments

# 8.14 Debugging

# 8.15 Glossary

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
