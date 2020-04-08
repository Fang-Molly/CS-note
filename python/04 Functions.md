# 4.1 Function calls

* function: a named sequence of statements that performs a computation
* define a function: specify the name and the sequence of statements
```
>>> type(32) 
<class 'int'>
```
* type function
   * function name: type
   * function argument: 32
   * function result: <class 'int'>

# 4.2 Built-in functions

* max() tells the largest value in a list
* min() tells the smallest value in a list

```
>>> max('Hello world')
'w'
>>> min('Hello world')
' '
```

* len() tells us how many items are in its argument

```
>>> len('Hello world')
11
```

* You should treat the names of built-in functions as reserved words 
   * i.e., avoid using “max” as a variable name.

# 4.3 Type conversion functions

* int() function: convert the value to an integer

```
>>> int('32')
32
>>> int('Hello')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'Hello'

# int() convert floating-point values to integers, but it doesn't round off; it chops off the fraction part
>>> int(3.999)
3
>>> int(-2.3)
-2

```
* float() function: convert integers and strings to floating-point numbers
```
>>> float(32)
32.0
>>> float('3.14159') 3.14159
```
* str() function: convert its argument to a string
```
>>> str(32)
'32'
>>> str(3.14159) 
'3.14159'
```

# 4.4 Math functions

* Python has a math module that provides most of the familiar mathmatical functions.
* **import math** before using the math module
* **dot notation** : separate the module name and the function name by a dot(.)

```
>>> import math
>>> print(math)
<module 'math' (built-in)>

# compute the square root of 5
>>> math.sqrt(5)
2.23606797749979

>>> radians = 0.7
>>> height = math.sin(radians)
>>> print(height)
0.644217687237691

>>> degrees = 45
>>> radians = degrees / 360.0 * 2 * math.pi >>> math.sin(radians)
0.7071067811865476
```

# 4.5 Random numbers

* Function random generate a random float between 0.0 and 1.0, including 0.0 but not 1.0.
```
>>> import random
>>> for i in range(10):
...    x = random.random()
...    print(x)
... 
0.8654079498088734
0.2911514211932603
0.6273732359608192
0.3735957581407181
0.8808868900172487
0.9844889557733428
0.2929450003717382
0.14267593228061592
0.7907418415244969
0.4643079930602618
```
* Function **randint** takes the parameters low and high, and returns an integer between low and high (including both)

```
>>> import random
>>> random.randint(5,10)
6
>>> random.randint(5,10)
7
```
* Function **choice** choose an element from a sequence at random

```
>>> import random
>>> t=[1,2,3]
>>> random.choice(t)
3
>>> random.choice(t)
2
```
* The random module also provides functions to generate random values from continuous distributions including **Gaussian, exponential, gamma, and a few more**.

# 4.6 Adding new functions

* **function definition** specifies the name of a new function
* **def** is a keyword that indicates that this is a function definition.
* function name
   * letters, numbers and some punctuation marks
   * first character can't be a number
   * can't use a keyword
   * can't use the same name for variable and function
* header: the first line of the function definition; 
   * the empty parentheses() after the name
   * end with a colon(:)
* body: the rest of the function definition; 
   * be indented, indentation is four spaces.
   * can contain any number of statements.
* the interpreter prints ellipses (...) to let you know the definition isn't complete

```
>>> def print_lyrics():
...     print("I'm a lumberjack, and I'm okay.") 
...     print('I sleep all night and I work all day.')
... 
>>> print_lyrics()
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
>>> 
>>> def repeat_lyrics(): 
...    print_lyrics() 
...    print_lyrics()
...    
>>> repeat_lyrics()
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day. 
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
```

# 4.7 Definitions and uses

```
>>> def print_lyrics():
...     print("I'm a lumberjack, and I'm okay.")
...     print('I sleep all night and I work all day.')
... 
>>> def repeat_lyrics():
...     print_lyrics()
...     print_lyrics()
... 
>>> repeat_lyrics()
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
```

# 4.8 Flow of execution

* **flow of execution** : the order in which statements are executed



# 4.9 Parameters and arguments

* **parameter** : the arguments are assigned to variables

```
>>> def print_twice(bruce):
...     print(bruce)
...     print(bruce)
... 
>>> print_twice('Spam')
Spam
Spam
>>> print_twice(17)
17
17

>>> import math
>>> print_twice(math.pi)
3.141592653589793
3.141592653589793

>>> print_twice('Spam '*4)
Spam Spam Spam Spam 
Spam Spam Spam Spam 

>>> print_twice(math.cos(math.pi))
-1.0
-1.0

>>> michael = 'Eric, the half a bee.'
>>> print_twice(michael)
Eric, the half a bee.
Eric, the half a bee.
```

# 4.10 Fruitful functions and void functions

* fruitful functions: such as the math functions, yield results

* void functions: perform an action but don't return a value
   * assign the result to a variable, you get a special value called None
   ```
   >>> result = print_twice('Bing')
   Bing
   Bing
   >>> print(result)
   None
   >>> print(type(None))
   <class 'NoneType'>
   ```

* **return** : return a result from a function
* **addtwo()** : add two numbers together and returns a result

```
>>> def addtwo(a, b):
...     added = a + b
...     return added
... 
>>> x = addtwo(3, 5)
>>> print(x)
8
```

# 4.11 Why functions?




# 4.12 Debugging




# 4.13 Glossary
