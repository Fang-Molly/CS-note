# 6.1 A string is a sequence

* **string** : a sequence of characters
* **extract the character** at index position n with the bracket operator [n]
   * index : the expression in brackets [ ], 
      * any expression, including variables and operators
      * the value has to be an integer, not 1.5
      * index[0] is the first letter, index[1] is the second
      * index[-1] is the last letter, index[-2] is the second to last
      
```
>>> fruit = 'banana'
>>> letter = fruit[1]
>>> print(letter)
a
```

# 6.2 Getting the length of a string using len

* **len()** : show the number of characters in a string

```
>>> fruit = 'banana'
>>> length = len(fruit)
>>> last = fruit[length-1]
>>> print(last)
a
```

# 6.3 Traversal through a string with a loop

* **traversal** 

    * while loop

   ```
   >>> index=0
   >>> while index<len(fruit):
   ...    letter=fruit[index]
   ...    print(letter)
   ...    index=index+1
   ... 
   b
   a
   n
   a
   n
   a
   >>> 
   ```
  
   * for loop
   
   ```
   >>> for char in fruit:
   ...     print(char)
   ... 
   b
   a
   n
   a
   n
   a
   >>>
   ```

# 6.4 String slices

* slice : a segment of a string

* The operator returns the part of the string from the “n-th” character to the “m-th” character, including the first but excluding the last.

```
>>> s = 'Monty Python'
>>> print(s[0:5])
Monty
>>> print(s[6:12])
Python
```
* omit the first index, the slice starts at the beginning
* omit the second index, the slice goes to the end

```
>>> fruit = 'banana'
>>> fruit[:3]
'ban'
>>> fruit[3:]
'ana'
>>> fruit[:]
'banana'
```

* if the first index >= the second, the result is an empty string.
* empty string 
   * contain no characters
   * length 0

```
>>> fruit = 'banana' 
>>> fruit[3:3]
''
```

# 6.5 Strings are immutable

* Strings are immutable, which means you can't change an existing string.

```
>>> greeting = 'Hello, world!'
>>> new_greeting = 'J' + greeting[1:]
>>> print(new_greeting)
Jello, world!
```

# 6.6 Looping and counting

* count the number of times the letter appears in a string

```
word = 'banana' 
count = 0
for letter in word:
    if letter == 'a': 
        count = count + 1
print(count)
```

# 6.7 The in operator

* word in is a boolean operator, returns True

```
>>> 'a' in 'banana'
True
>>> 'seed' in 'banana'
False
```


# 6.8 String comparison




# 6.9 String methods

* dir function : list the methods available for an object.
* type function : show the type of an object
```
>>> stuff = 'Hello world'
>>> type(stuff)
<class 'str'>
>>> dir(stuff)
['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(str.capitalize) Help on method_descriptor:
```
* **method upper/lower** takes a string and returns a new string with all uppercase letters

```
>>> word = 'banana'
>>> new_word = word.upper()
>>> print(new_word)
```
* **methond find** search for the position of one string within another
```
>>> word = 'banana'
>>> index = word.find('a')
>>> print(index)
1
```

* **method strip** remove white space (space, tabs, or newlines) from the beginning and end or a string

```
>>>line=' Herewego ' 
>>> line.strip()
'Here we go'
```
* **method startswith** return boolean values, require case to match

```
>>> line = 'Have a nice day' 
>>> line.startswith('Have') 
True
>>> line.startswith('h') 
False
>>> line.lower()
'have a nice day'
>>> line.lower().startswith('h') 
True
```

# 6.10 Parsing strings

# 6.11 Format operator


# 6.12 Debugging

# 6.13 Glossary

* **counter** A variable used to count something, usually initialized to zero and then incremented.

* **empty string** A string with no characters and length 0, represented by two quo- tation marks.

* **format operator** An operator, %, that takes a format string and a tuple and gen- erates a string that includes the elements of the tuple formatted as specified by the format string.

* **format sequence** A sequence of characters in a format string, like %d, that spec- ifies how a value should be formatted.

* **format string** A string, used with the format operator, that contains format sequences.

* **flag** A boolean variable used to indicate whether a condition is true or false. 

* **invocation** A statement that calls a method.

* **immutable** The property of a sequence whose items cannot be assigned.

* **index** An integer value used to select an item in a sequence, such as a character in a string.

* **item** One of the values in a sequence.

* **method** A function that is associated with an object and called using dot notation.

* **object** Something a variable can refer to. For now, you can use “object” and “value” interchangeably.

* **search** A pattern of traversal that stops when it finds what it is looking for. 

* **sequence** An ordered set; that is, a set of values where each value is identified by an integer index.

* **slice** A part of a string specified by a range of indices.

* **traverse** To iterate through the items in a sequence, performing a similar operation on each.
