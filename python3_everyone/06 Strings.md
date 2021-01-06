# Chapter 6  Strings

## 6.1 A string is a sequence

* **String** : a sequence of characters

```python
# a string literal uses single or double quotes
>>> str1 = "Hello"
>>> str2 = 'there'

# concatenate strings using + operator
>>> bob = str1 + str2
>>> print(bob)
Hellothere
>>> bob = str1 + ' ' + str2
>>> print(bob)
Hello there

# When a string contains numbers, it is still a string
>>> str3 = '123'
>>> str4 = str3 + 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str

# convert numbers in a string into a number using int()
>>> str4 = int(str3) + 1
>>> print(str4)
124

# Input numbers must be converted from strings
>>> apple = input('Enter: ')
Enter: 100
>>> x = apple - 10
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> x = int(apple) - 10
>>> print(x)
90
```

* **String Index** - the expression in square brackets[ ]      

   * The index value must be an integer and starts at zero.
      * index[0] is the first letter, index[1] is the second
      * index[-1] is the last letter, index[-2] is the second to last
      
   * The index value can be an expression that is computed, including variables and operators     
   
b---a---n---a---n---a    
[0]-[1]-[2]-[3]-[4]-[5]     
[-6][-5][-4][-3][-2][-1]
 
* **extract the character** at index position n with the bracket operator [n]

```python
>>> fruit = 'banana'

# get the first letter of a string
>>> letter = fruit[0]
>>> print(letter)
b

# get the last letter of a string
>>> last = fruit[-1]
>>> print(last)
>>> a

# the index is an expression
>>> x = 3
>>> w = fruit[x - 1]
>>> print(w)
n

# you can't index beyond the length of the string
>>> print(fruit[6])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> 
```

## 6.2 Getting the length of a string using `len`

* **`len()`** : built-in function, returns the number of characters in a string

```python
# get the number of characters in a string
>>> fruit = 'banana'
>>> len(fruit)
>>> 6

# get the last letter of a string
>>> length = len(fruit)
>>> last = fruit[length-1]   # last = fruit[-1]
>>> print(last)
a
```

## 6.3 Traversal through a string with `while` and `for` loop

* **traversal**: A lot of computations involve processing a string one character at a time. Often they start at the beginning, select each character in turn, do something to it, and continue until the end. This pattern of processing is called a traversal.   

* **`while` loop** - indeterminate loop

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
  
* **`for` loop** - determinant loop
   
```python
>>> fruit = 'banana'
>>> for letter in fruit:
...     print(letter)
... 
b
a
n
a
n
a
>>>
```
* `while` and `for` loop is equal, we generally prefer a `for` loop

## 6.4 Looping and counting

* count the number of times the letter appears in a string

```python
word = 'banana' 
count = 0
for letter in word:
    if letter == 'a': 
        count = count + 1
print(count)
```
   
## 6.5 String slices

* **slice : a segment of a string**

* The **colon(`:`) operator** returns any continuous section of a string
   * **up to but not including** - start at posion the first number, but not including the last number position.

```python
>>> s = 'Monty Python'

# The second number is one up to but not including.
>>> print(s[0:4])
Mont
>>> print(s[6:7])
P

# If the second number is beyond the end of the string, it stops at the end.
>>> print(s[6:20])
Python

# omit the first index, the slice starts at the beginning
>>> print(s[:2])
Mo

# omit the second index, the slice goes to the end
>>> print(s[8:])
thon

# omit the first and second index, the slice starts at the beginning and goes to the end
>>> print(s[:])
Monty Python

# if the first index >= the second, the result is an empty string, represented by two quotation marks.
# empty string: contain no characters; length is 0
>>> print(s[3:3])
''
```

## 6.6 Strings are immutable

* Strings are immutable, you can't change an existing string.

```python
>>> greeting = 'Hello, world!'
>>> greeting[0] = 'J'
TypeError: 'str' object does not support item assignment

# strings concatenation generates new strings
>>> greeting = 'Hello, world!'
>>> new_greeting = 'J' + greeting[1:]
>>> print(new_greeting)
Jello, world!
```

## 6.7 Using `in` as a logical operator

* The keyword `in` is a boolean operator that takes two strings and returns `True` if the first appears as a substring in the second
* can be used in `if` statement

```python
>>> fruit = 'banana'

# boolean operator, returns True or False
>>> 'a' in fruit
True
>>> 'seed' in fruit
False

# in can be used in if statement
>>> if 'a' in fruit:
...    print('Found it!')
...
Found it!
>>>
```

## 6.8 String comparison

* The comparison operators work on strings. Be useful for putting words in alphabetical order

* Python does not handle uppercase and lowercase letters the same way that people do. **All the uppercase letters come before all the lowercase letters**

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

* **object** : Strings are an example of Python objects. An object contains both data and methods, which are effectively functions that are built into the object and are available to any instance of the object.

```python
>>> stuff = 'Hello world'

# type function shows the type of an object
>>> type(stuff)
<class 'str'>

# dir function shows the a  vailable methods
>>> dir(stuff)
['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

# help function shows some simple documentation on a method
>>> help(str.capitalize) 

Help on method_descriptor:

capitalize(self, /)
    Return a capitalized version of the string.
    
    More specifically, make the first character have upper case and the rest lower
    case.    
```

* **method upper/lower** takes a string and returns a new string with all uppercase or lowercase letters

```python
# string.upper(), string.lower()
>>> word = 'banana'
>>> new_word = word.upper()
>>> print(new_word)
BANANA
```
* **methond find** search for the position of one string within another

```python
# string.find()
>>> word = 'banana'
>>> index = word.find('a')
>>> print(index)
1

# find substring
>>> word.find('na')
2

# If the substring is not found, retruns -1
>>> aa = word.find('z')
>>> print(aa)
-1

# take as a second argument the index where it should start
>>> word.find('na', 3)
4
```

* **method replace** - like a "search and replace" operation in a word processor

```python
>>> greet = 'Hello Bob'
>>> nstr = greet.replace('Bob','Jane')
>>> print(nstr)
Hello Jane
>>> nstr = greet.replace('o','x')
>>> print(nstr)
Hellx Bxb
>>> 
```

* **method strip** remove white space (space, tabs, or newlines) from the beginning and end or a string

```python
>>> greet = '  Hello Bob  '

# string.lstrip() remove whitespace at the left 
>>> greet.lstrip()
'Hello Bob  '

# string.rstrip() remove whitespace at the right
>>> greet.rstrip()
'  Hello Bob'

# string.strip() remove both beginning and ending whitespace
>>> greet.strip()
'Hello Bob'
>>> 
```

* **method startswith** : return boolean values, require case to match

```python
# string.startswith()
>>> line = 'Have a nice day' 
>>> line.startswith('Have') 
True
# case sensitive
>>> line.startswith('h') 
False
>>> line.lower()
'have a nice day'
>>> line.lower().startswith('h') 
True
```

## 6.10 Parsing strings

* **Find, slice and extract the characters from the string**

```python
>>> data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
>>> atpos = data.find('@')
>>> print(atpos)
21
>>> sppos = data.find(' ', atpos)
>>> print(sppos)
31
>>> host = data[atpos+1 : sppos]
>>> print(host)
uct.ac.za
>>> 
```

## 6.11 Format operator

* **format operator (`%`)** : construct strings, replacing parts of the strings with the data stored in variables.

   * **`%d` format an integer, d stands for decimal.**
   
   * **`%g` format a floating-point number**
   
   * **`%s` format a string**
   
   * **`%r` format any you type**
   
* **Format syntax** :
   
   * **first operand**: a string, the format string, specify how the second operand is formmated
   * **second operand**: can be an integer, a floating-point number, a string, any type, or a tuple ()
   * **result**: a string
   
```python
>>> camels = 42
>>> "I have spotted %d camels." % camels
'I have spotted 42 camels.'

# multiple formats: a tuple, put in parentheses (), separated by commas (,)
>>> "In %d years I have spotted %g %s." % (3, 0.1, 'camels')
'In 3 years I have spotted 0.1 camels.'

# the number of elements in the tuple must match the number of format sequences in the string
>>> '%d %d %d' % (1,2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: not enough arguments for format string

# the types of the elements also must match the format sequences
>>> '%d' % 'dollars'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: %d format: a number is required, not str
```
* **Anothe format type**
   * format string: special {} sequence
      * start the string with the letter f
      
```python
my_name = 'Alice'
Print(f"Let's talk about {my_name}.")
```
--------------------------

# Glossary

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

------------------

# Exercises

**Exercise 1: Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.**

**Answer:**

```python
fruit = 'banana'
index = 0
while index >= (0 - len(fruit)):
    letter = fruit[index-1]
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

**Exercise 4: There is a string method called count that is similar to the function in the previous exercise. Read the documentation of this method at: https://docs.python.org/library/stdtypes.html#string-methods. Write an invocation that counts the number of times the letter a occurs in “banana”.**   

**Answer:**

```python
>>> word = 'banana'
>>> word.count('a')
3
>>> word.count('a', 1, 5)
2
```

**Exercise 5: Take the following Python code that stores a string:**

str = 'X-DSPAM-Confidence:0.8475'

Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.

**Answer:**

```python
str = 'X-DSPAM-Confidence:0.8475'
startpos = str.find(':')
piece = str[startpos+1:]
value = float(piece)
print(value)
```

**Exercise 6: Read the documentation of the string methods at https://docs.python.org/library/stdtypes.html#string-methods You might want to experiment with some of them to make sure you understand how they work. strip and replace are particularly useful.**

The documentation uses a syntax that might be confusing. For example, in find(sub[, start[, end]]), the brackets indicate optional arguments. So sub is required, but start is optional, and if you include start, then end is optional.



