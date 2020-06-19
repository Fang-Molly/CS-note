# Chapter 6  Strings

## 6.1 A string is a sequence

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
* b | a | n | a | n | a    
 [0] [1] [2] [3] [4] [5]   
 [-6][-5][-4][-3][-2][-1]

## 6.2 Getting the length of a string using len

* **len()** : show the number of characters in a string

```
>>> fruit = 'banana'
>>> len(fruit)
>>> 6
>>> length = len(fruit)
>>> last = fruit[length-1]
>>> print(last)
a
```

## 6.3 Traversal through a string with a loop

* **traversal**: A lot of computations involve processing a string one character at a time. Often they start at the beginning, select each character in turn, do something to it, and continue until the end. This pattern of processing is called a traversal.   

    * **while loop**

   ```python
   >>> fruit = 'banana'
   >>> index = 0
   >>> while index < len(fruit):
   ...    letter = fruit[index]
   ...    print(letter)
   ...    index = index + 1
   ... 
   b
   a
   n
   a
   n
   a
   >>> 
   ```
  
   * **for loop**
   
   ```python
   >>> fruit = 'banana'
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

## 6.4 String slices

* **slice : a segment of a string**

* The operator returns the part of the string from the “n-th” character to the “m-th” character, including the first but excluding the last

```python
>>> s = 'Monty Python'
>>> print(s[0:5])
Monty
>>> print(s[6:12])
Python
```
* omit the first index, the slice starts at the beginning
* omit the second index, the slice goes to the end
* omit the first and second index, the slice starts at the beginning and goes to the end

```python
>>> fruit = 'banana'
>>> fruit[:3]
'ban'
>>> fruit[3:]
'ana'
>>> fruit[:]
'banana'
```

* if the first index >= the second, the result is an empty string, represented by two quotation marks.
* empty string 
   * contain no characters
   * length 0

```
>>> fruit = 'banana' 
>>> fruit[3:3]
''
```

## 6.5 Strings are immutable

* Strings are immutable, you can't change an existing string.

```
>>> greeting = 'Hello, world!'
>>> greeting[0] = 'J'
TypeError: 'str' object does not support item assignment

>>> greeting = 'Hello, world!'
>>> new_greeting = 'J' + greeting[1:]
>>> print(new_greeting)
Jello, world!
```

## 6.6 Looping and counting

* count the number of times the letter appears in a string

```
word = 'banana' 
count = 0
for letter in word:
    if letter == 'a': 
        count = count + 1
print(count)
```

## 6.7 The in operator

* The word in is a boolean operator that takes two strings and returns True if the first appears as a substring in the second

```python
>>> 'a' in 'banana'
True
>>> 'seed' in 'banana'
False
```

## 6.8 String comparison

* The comparison operators work on strings. Be useful for putting words in alphabetical order

* thon does not handle uppercase and lowercase letters the same way that people do. All the uppercase letters come before all the lowercase letters

```python
word = input('Enter your word: ')
if word == 'banana':
    print('All right, bananas.')
elif word < 'banana':
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('Please rerun again')
```

## 6.9 String methods

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

* format operator: % construct strings, replacing parts of the strings with the data stored in variables.

   * %d : format an integer, d stands for decimal.
   
   ```
   >>> camels = 42
   >>> "I have spotted %d camels." % camels
   'I have spotted 42 camels.'
   ```
   * %g format a floating-point number
   
   * %s format a string
   
   * %r format any you type
   
   ```
   >>> "In %d years I have spotted %g %s." % (3, 0.1, 'camels')
   'In 3 years I have spotted 0.1 camels.'
   ```
   *  multiple formats: put in parentheses (), separated by commas(,)
   
   * The number of elements in the tuple must match the number of format sequences in the string. The types of the elements also must match the format sequences
   
   ```
   >>> '%d %d %d' % (1, 2)
   TypeError: not enough arguments for format string >>> '%d' % 'dollars'
   TypeError: %d format: a number is required, not str
   ```

* format string: special {} sequence
   * start the string with the letter f
```
my_name = 'Alice'
Print(f"Let's talk about {my_name}.")

```

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


**Exercise 1: Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.**

**Answer:**

```python
fruit = 'banana'
index = -1
while index >= (0 - len(fruit)):
    letter = fruit[index]
    print(letter)
    index = index - 1   
```

**Exercise 2: Given that fruit is a string, what does fruit[:] mean?**

**Answer:**

```python
>>> fruit = 'banana'
>>> fruit[:]
'banana'
```
**Exercise 3: Encapsulate this code in a function named count, and gen- eralize it so that it accepts the string and the letter as arguments.**

**Answer:**

```python

def count(string, letter):
    counter = 0
    for character in string:
        if character == letter:
            counter = counter + 1
    print(counter)

input_string = input('Enter the word: ')
input_letter = input('Enter the letter: ')
count(input_string, input_letter)
```
