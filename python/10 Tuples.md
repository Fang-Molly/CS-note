# Chapter 10  Tuples

## 10.1 Tuples are immutable

* **tuple**
   * a sequence of values much like a list
   * the values can be any type
   * be indexed by integers
   * be immutable
   * be comparable and hashable
      * can sort lists of them
      * use tuples as key values in dictionaries
      
* **syntax of tuple**
   * element enclosed by ''
   * all the elements enclosed by parentheses commonly, not necessarily. Be helpfyl to identify tuples
```
>>> t = 'a', 'b', 'c', 'd', 'e'
>>> t = ('a', 'b', 'c', 'd', 'e')
```
   * have to include the final comma when a tuple has a single element; Without comma, the type is string

```
>>> t1 = ('a',)
>>> type(t1)
<class 'tuple'>
>>> t2 = ('a')
>>> type(t2)
<class 'str'>
```

* **built-in function tuple**: another way to construct a tuple
```
>>> t = tuple()
>>> print(t)
()
```
```
>>> t = tuple('lupins')
>>> print(t)
('l', 'u', 'p', 'i', 'n', 's')
```

* tuple can't be used as a variable name.

* operator works on tuples
```
>>> t = ('a', 'b', 'c', 'd', 'e')
>>> print(t[0])
a
>>> print(t[1:3])
('b', 'c')
```

* can't modify the elements of a tuple, you can replace one tuple with another
```
>>> t[0] = 'A'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> t = ('A',) + t[1:]
>>> print(t)
('A', 'b', 'c', 'd', 'e')
```
## 10.2 Comparing tuples

* Comparing starts by the first element from each sequence. 
* If they are equal, it goes on to the next element, and so on, until it finds elements that differ. 
* Subsuquent elements are not considered.

```
>>> (0, 1, 2) < (0, 3, 4)
True
>>> (0, 1, 2000000) < (0, 3, 4)
True
```
> sort function: primarily by first element, if it is equal, then by second element, and so on
> DSU pattern: decorate, sort, undecorate



