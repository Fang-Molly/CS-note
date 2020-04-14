# 8.1 A list is a sequence

* list : a sequence of values
   * element or item : the values can be any type

* create a new list
   * enclose the elements in square brackets([ ])
      * a list of four integers [10, 20, 30, 40]
      * a list of strings ['crunchy frog', 'ram bladder', 'lark vomit']
      * a list of multiple types ['spam', 2.0, 5, [10, 20]]
   * nested : a list within another list
   * an empty list: a list contains no elements, with empty brackets []

* assign list values to variables
```
>>> cheeses = ['Cheddar', 'Edam', 'Gouda'] 
>>> numbers = [17, 123]
>>> empty = []
>>> print(cheeses, numbers, empty) 
['Cheddar', 'Edam', 'Gouda'] [17, 123] []
```      
# 8.2 Lists are mutable

* access the elements of a list
   * the index of a list start at 0

```
>>> cheeses = ['Cheddar', 'Edam', 'Gouda']
>>> print(cheeses[0])
Cheddar
```
* reassign an item in a list

```
>>> numbers = [17, 123]
>>> numbers[1] = 5
>>> print(numbers)
[17, 5]
```
* **in operator**

```
>>> cheeses = ['Cheddar', 'Edam', 'Gouda']
>>> 'Edam' in cheeses
True
>>> 'Brie' in cheeses
False
```

# 8.3 Traversing a list

* **for loop** : read the elements of the list

```
>>> cheeses = ['Cheddar', 'Edam', 'Gouda']
>>> for cheese in cheeses:
...     print(cheese)
... 
Cheddar
Edam
Gouda

>>> cheeses = ['Cheddar', 'Edam', 'Gouda']
>>> print(cheeses)
['Cheddar', 'Edam', 'Gouda']
```
* write or update the elements, need the indices, combine the functions range and len





# 8.4 List operations

* **+ operator** concatenates lists

```
>>> a = [1, 2, 3]
>>> b = [4, 5, 6]
>>> c = a + b
>>> print(c)
[1, 2, 3, 4, 5, 6]
```
* ** * operator** repeats a list 

# 8.5 List slices








# 8.6 List methods

# 8.7 Deleting elements

# 8.8 Lists and functions

# 8.9 Lists and strings

# 8.10 Parsing lines

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
