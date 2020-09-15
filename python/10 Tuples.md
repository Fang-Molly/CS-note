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














