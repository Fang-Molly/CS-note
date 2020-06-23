* **str.capitalize(): Return a copy of the string with its first character capitalized and the rest lowercased.**

```python
>>> str = 'hello world'
>>> str.capitalize()
'Hello world'
```

* **str.casefold(): Return a casefolded copy of the string. Casefolding is similar to lowercasing but more aggressive because it is intended to remove all case distinctions in a string. **

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

* **str.expandtabs(tabsize=8)：Return a copy of the string where all tab characters are replaced by one or more spaces, depending on the current column and the given tab size.**

```python
>>> str = 'H\te\tl\tl\to'
>>> str.expandtabs(2)
'H e l l o'
>>> str.expandtabs()
'H       e       l       l       o'
```

* **str.find(sub[, start[, end]]): Return the lowest index in the string where substring sub is found within the slice s[start:end].**

```python
>>> str = 'Hello, welcome to my world.'
>>> str.find('welcome')
7
>>> str.find('e', 5, 10)
8
```

* **str.format(*args, **kwargs): Perform a string formatting operation. The string on which this method is called can contain literal text or replacement fields delimited by braces {}.**

```python
>>> str = 'For only {price:.2f} dollars!'
>>> print (str.format(price = 49))
For only 49.00 dollars!

>>> str1 = "My name is {name}, I'm {age}"
>>> str1.format(name = 'John', age = 36)
"My name is John, I'm 36"
>>> str2 = "My name is {0}, I'm {1}"
>>> str2.format('John', 36)
"My name is John, I'm 36"
>>> str3 = "My name is {}, I'm {}"
>>> str3.format('John', 36)
"My name is John, I'm 36"
```

* **str.format_map(mapping): Similar to str.format(**mapping), except that mapping is used directly and not copied to a dict.**

* **str.index(sub[, start[, end]]): Like find(), but raise ValueError when the substring is not found.**

```python
>>> str = "Hello, Welcome to my world."
>>> str.index('e')
1
>>> str.index('e', 5, 10)
8
```

* **str.isalnum(): Return True if all characters in the string are alphanumeric and there is at least one character, False otherwise.**

```python
>>> str = 'Company12'
>>> str.isalnum()
True
```

* **str.isalpha(): Return True if all characters in the string are alphabetic and there is at least one character, False otherwise.

```python
>>> str = 'CompanyX'
>>> str.isalpha()
True
```

* **str.isascii(): Return True if the string is empty or all characters in the string are ASCII, False otherwise.

* **str.isdecimal(): Return True if all characters in the string are decimal characters and there is at least one character, False otherwise.**

* **str.isdigit(): Return True if all characters in the string are digits and there is at least one character, False otherwise.

* **str.isidentifier(): Return True if the string is a valid identifier according to the language definition, section Identifiers and keywords.

* **str.islower(): Return True if all cased characters 4 in the string are lowercase and there is at least one cased character, False otherwise.

```python
>>> str = "hello world!"
>>> str.islower()
True
>>> str = "hello 123"
>>> str.islower()
True
>>> str = "mynameisPeter"
>>> str.islower()
False
```
* **str.isnumeric(): Return True if all characters in the string are numeric characters, and there is at least one character, False otherwise.

* **str.isprintable(): Return True if all characters in the string are printable or the string is empty, False otherwise. 

* **str.isspace(): Return True if there are only whitespace characters in the string and there is at least one character, False otherwise.


* **str.istitle(): Return True if the string is a titlecased string and there is at least one character, for example uppercase characters may only follow uncased characters and lowercase characters only cased ones. Return False otherwise.

* **str.isupper(): Return True if all cased characters 4 in the string are uppercase and there is at least one cased character, False otherwise.**

* **str.join(iterable): Return a string which is the concatenation of the strings in iterable. 

```python
>>> myTuple = ("John", "Peter", "Vicky")
>>> "#".join(myTuple)
'John#Peter#Vicky'
```

* **str.ljust(width[, fillchar]): Return the string left justified in a string of length width. **

* **str.lower(): Return a copy of the string with all the cased characters 4 converted to lowercase.**


* **str.lstrip([chars]): Return a copy of the string with leading characters removed. The chars argument is a string specifying the set of characters to be removed.**

* **static str.maketrans(x[, y[, z]]): This static method returns a translation table usable for str.translate().**


* **str.partition(sep): Split the string at the first occurrence of sep, and return a 3-tuple containing the part before the separator, the separator itself, and the part after the separator. 

* **str.replace(old, new[, count]): Return a copy of the string with all occurrences of substring old replaced by new. 

* **str.rfind(sub[, start[, end]]): Return the highest index in the string where substring sub is found, such that sub is contained within s[start:end]. 


* **str.rindex(sub[, start[, end]]): Like rfind() but raises ValueError when the substring sub is not found.**


* **str.rjust(width[, fillchar]): Return the string right justified in a string of length width. 


* **str.rpartition(sep): Split the string at the last occurrence of sep, and return a 3-tuple containing the part before the separator, the separator itself, and the part after the separator. 

* **str.rsplit(sep=None, maxsplit=-1): Return a list of the words in the string, using sep as the delimiter string. 

* **str.rstrip([chars]): Return a copy of the string with trailing characters removed.** 


* **str.split(sep=None, maxsplit=-1): Return a list of the words in the string, using sep as the delimiter string.**

```python
>>> str = "welcome to the jungle"
>>> str.split()
['welcome', 'to', 'the', 'jungle']
>>> str = "hello, my name is Peter, I am 26 years old"
>>> str.split(", ")
['hello', 'my name is Peter', 'I am 26 years old']
```

* **str.splitlines([keepends]): Return a list of the lines in the string, breaking at line boundaries. Line breaks are not included in the resulting list unless keepends is given and true.**

```python
>>> str = "Thank you for the music\nWelcome to the jungle"
>>> str.splitlines()
['Thank you for the music', 'Welcome to the jungle']
>>> str.splitlines(True)
['Thank you for the music\n', 'Welcome to the jungle']
```

Representation | Description
|:--           |:--             |
\n             | Line Feed
\r             | Carriage Return
\r\n           | Carriage Return + Line Feed
\v or \x0b     | Line Tabulation
\f or \x0c     | Form Feed
\x1c           | File Separator
\x1d           | Group Separator
\x1e           | Record Separator
\x85           | Next Line (C1 Control Code)
\u2028         | Line Separator
\u2029         | Paragraph Separator


* **str.startswith(prefix[, start[, end]]): Return True if string starts with the prefix, otherwise return False. **

```python
>>> str = "Hello, welcome to my world."
>>> str.startswith("Hello")
True
```

* **str.strip([chars]): Return a copy of the string with the leading and trailing characters removed. **

```python
>>> str = "     banana     "
>>> str.strip()
'banana'
>>> str = ",,,,,rrttgg.....banana....rrr"
>>> str.strip(",.grt")
'banana'
>>> str = "www.example.com"
>>> str.strip('cmowz.')
'example'
>>> str = "#....... Section 3.2.1 Issue #32 ......."
>>> str.strip('.#! ')
'Section 3.2.1 Issue #32'
```
* **str.swapcase(): Return a copy of the string with uppercase characters converted to lowercase and vice versa. **

```python
>>> str = 'Hello My Name Is PETER'
>>> str.swapcase()
'hELLO mY nAME iS peter'
```

* **str.title(): Return a titlecased version of the string where words start with an uppercase character and the remaining characters are lowercase.**

```python
>>> str = 'Welcome to my world'
>>> str.title()
'Welcome To My World'
```

* **str.translate(table): Return a copy of the string in which each character has been mapped through the given translation table.**



* **str.upper(): Return a copy of the string with all the cased characters 4 converted to uppercase.**

```python
>>> str = 'Hello my friends'
>>> str.upper()
'HELLO MY FRIENDS'
```

* **str.zfill(width): Return a copy of the string left filled with ASCII '0' digits to make a string of length width.**

```python
>>> "42".zfill(5)
'00042'
>>> "-42".zfill(5)
'-0042'
```
