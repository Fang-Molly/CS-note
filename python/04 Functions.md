# Chapter 4  Functions

## 4.1 Function Definition

* **function**: some *reusable* code that takes *arguments* as input, does some computation, and then returns a result or results

* define a function: using the `def` reserved word to specify the name and the sequence of statements

* call/invoke the function: using the function name, parentheses, and arguments in an expression

* **Function types:**

   * Built-in functions: print(), input(), type(), float(), int()...
      * We treat the built-in function names as "new" reserved words. (i.e., avoid them as variable names.)
   
   * New functions that we define ourselves

## 4.2 Built-in functions

* **type() function**

```python
>>> type(32) 
<class 'int'>
```

* **max() function** - tells the largest value in a list

* **min() function** - tells the smallest value in a list

```python
>>> max('Hello world')
'w'
>>> min('Hello world')
' '
```

* **len() function** - tells us how many items are in its argument

```python
>>> len('Hello world')
11
```

* You should treat the names of built-in functions as reserved words 
   * i.e., avoid using “max” as a variable name.

## 4.3 Type conversion functions

* **int() function** - convert the value to an integer

```python
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

* **float() function** - convert integers and strings to floating-point numbers

```python
>>> float(32)
32.0
>>> float('3.14159') 
3.14159
```

* **str() function** - convert its argument to a string

```python
>>> str(32)
'32'
>>> str(3.14159) 
'3.14159'
```

## 4.4 Math functions

* **`math` module** - provides most of the familiar mathmatical functions in Python

   * **`import math`** - before using the math module

```python
>>> import math

>>> print(math)
<module 'math' (built-in)>
```

   * **dot notation** - separate the module name and the function name by a dot(.)

* `math.log10()`

```python
>>> ratio = signal_power / noise_power
>>> decibels = 10 * math.log10(ratio)
```

* `math.sqrt()`

```python
# compute the square root of 5
>>> math.sqrt(5)
2.23606797749979
```
* `math.sin()`

```python
>>> radians = 0.7
>>> height = math.sin(radians)
>>> print(height)
0.644217687237691
```

* `math.pi`

```pyton
>>> degrees = 45
>>> radians = degrees / 360.0 * 2 * math.pi >>> math.sin(radians)
0.7071067811865476
```

## 4.5 Random numbers

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

## 4.6 Adding new functions

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

## 4.7 Definitions and uses

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

## 4.8 Flow of execution

* **flow of execution** : the order in which statements are executed



## 4.9 Parameters and arguments

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

## 4.10 Fruitful functions and void functions

* **fruitful functions**: such as the math functions, yield results

* **void functions**: perform an action but don't return a value
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

```
>>> def addtwo(a, b):
...     added = a + b
...     return added
... 
>>> x = addtwo(3, 5)
>>> print(x)
8
```

## 4.11 Why functions?

* the reasons to divide a program into functions:

   1. It makes your program easier to read, understand and debug
   2. It makes your program smaller by eliminating repetitive code
   3. It makes earier to dubug the parts one at a time and assemble them into a working whole
   4. It makes earier to write, debug and reuse

## 4.12 Debugging

* ues spaces exclusively (no tabs) to avoid problems with spaces and tabs.

* Don't forget to save your program before you run it.

## 4.13 Glossary

* **algorithm** A general process for solving a category of problems.

* **argument** A value provided to a function when the function is called. This value is assigned to the corresponding parameter in the function.

* **body** The sequence of statements inside a function definition.

* **composition** Using an expression as part of a larger expression, or a statement as part of a larger statement.

* **deterministic** Pertaining to a program that does the same thing each time it runs, given the same inputs.

**dot notation** The syntax for calling a function in another module by specifying the module name followed by a dot (period) and the function name.

**flow of execution** The order in which statements are executed during a program run.

**fruitful function** A function that returns a value.

**function** A named sequence of statements that performs some useful operation. Functions may or may not take arguments and may or may not produce a result.

**function call** A statement that executes a function. It consists of the function name followed by an argument list.

**function definition** A statement that creates a new function, specifying its name, parameters, and the statements it executes.

**function object** A value created by a function definition. The name of the function is a variable that refers to a function object.

**header** The first line of a function definition.

**import statement** A statement that reads a module file and creates a module object.

**module object** A value created by an import statement that provides access to the data and code defined in a module.

**parameter** A name used inside a function to refer to the value passed as an argument.

**pseudorandom** Pertaining to a sequence of numbers that appear to be random, but are generated by a deterministic program.

**return value** The result of a function. If a function call is used as an expression, the return value is the value of the expression. 

**void function** A function that does not return a value.

## 4.14 Exercises

**Exercise 1: Run the program on your system and see what numbers you get. Run the program more than once and see what numbers you get.**

import random

for i in range(10):
    x = random.random() 
    print(x)



**Exercise 2: Move the last line of this program to the top, so the function call appears before the definitions. Run the program and see what error message you get.**

```python
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.") 
    print('I sleep all night and I work all day.')
def repeat_lyrics(): 
    print_lyrics() 
    print_lyrics()

repeat_lyrics()
```

**Answer:**

```python
repeat_lyrics()

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

def repeat_lyrics():
    print_lyrics()
    print_lyrics()
    
Traceback (most recent call last):
  File "chapter4_ex2.py", line 1, in <module>
    repeat_lyrics()
NameError: name 'repeat_lyrics' is not defined
```


**Exercise 3: Move the function call back to the bottom and move the definition of print_lyrics after the definition of repeat_lyrics. What happens when you run this program?**

```python
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.") 
    print('I sleep all night and I work all day.')
def repeat_lyrics(): 
    print_lyrics() 
    print_lyrics()

repeat_lyrics()
```

**Answer:**

```python
def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

repeat_lyrics()

I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
```


**Exercise 4: What is the purpose of the “def” keyword in Python?**

a) It is slang that means “the following code is really cool”  
b) It indicates the start of a function  
c) It indicates that the following indented section of code is to be stored for later  
d) b and c are both true  
e) None of the above  

**Answer:**
e


**Exercise 5: What will the following Python program print out?**

```python
def fred():  
    print("Zap")  
    
def jane(): 
    print("ABC")
    
jane()
fred()
jane()
```
a) Zap ABC jane fred jane  
b) Zap ABC Zap  
c) ABC Zap jane  
d) ABC Zap ABC  
e) Zap Zap Zap  

**Answer:**
d


**Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).**

Enter Hours: 45   
Enter Rate: 10    
Pay: 475.0   

**Answer:**

```python
hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

if int(hours) <= 40:
    def computepay(hours, rate):
        wages = int(hours) * int(rate)
        return wages
    x = computepay(hours, rare)
    print('Pay: ', x)
else:
    def computepay(hours, rate):
        wages =(int(hours)-40) * int(rate) * 1.5 + 40 * int(rate)
        return wages
    x = computepay(hours, rate)
    print('Pay: ', x)
```


**Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.**
Score  Grade  
>= 0.9  A   
>= 0.8  B   
>= 0.7  C   
>= 0.6  D  
<0.6    F  

Enter score: 0.95    
A  

Enter score: perfect  
Bad score  

Enter score: 10.0  
Bad score  

Enter score: 0.75   
C

Enter score: 0.5   
F  

Run the program repeatedly to test the various different values for input.

**Answer:**

```python
score = input('Please enter a score between 0.0 and 1.0: ')
try:
    def computegrade():
        if float(score) >= 0.9 and float(score) <= 1.0:
            print('A')
        elif float(score) >= 0.8 and float(score) < 0.9:
            print('B')
        elif float(score) >= 0.7 and float(score) < 0.8:
            print('C')
        elif float(score) >= 0.6 and float(score) < 0.7:
            print('D')
        elif float(score) < 0.6 and float(score) >= 0.0:
            print('F')
        else:
            print('Bad score')
    computegrade()
except:
    print('Bad score')
```
