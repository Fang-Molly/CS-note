* **str.capitalize(): Return a copy of the string with its first character capitalized and the rest lowercased.**

```python
>>> str = 'hello world'
>>> str.capitalize()
'Hello world'
```

* **str.casefold(): Return a casefolded copy of the string.**

```python
>>> str = 'Hello World'
>>> str.casefold()
'hello world'
```

* **str.center(width[, fillchar]): Return centered in a string of length width.**

```python
>>> str = 'banana'
>>> str.center(20)
'       banana       '
```

* **str.count(sub[, start[, end]]): Return the number of non-overlapping occurrences of substring sub in the range [start, end].**

```python
>>> str = 'banana'
>>> str.count('a', 1, 5)
2
```

* **str.encode(encoding="utf-8", errors="strict"): Return an encoded version of the string as a bytes object.**

```python
>>> str = 'My name is Lisa'
>>> str.encode()
b'My name is Lisa'
```
* **str.endswith(suffix[, start[, end]]): Return True if the string ends with the specified suffix, otherwise return False.**

```python
>>> str = 'Hello, welcome to my world.'
>>> str.endswith('.')
True
```



