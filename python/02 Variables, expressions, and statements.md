# 2.1 Values and types
+ **value** : a letter or a number
+ **types**
   + **integer**: type ```int```; 2
   + **string**: type ```str```; 
      * enclosed in " double-quotes or ' single-quotes.
      * "Hello, World!"; "17"; "3.2"
   + **floating point**: type ```float```; 3.2
   
   ----
   
   ```
   # print() for integers
   >>> print(4)
   4
   
   # print() for strings
   >>> print("Hello, World!")
   Hello, World!
   >>> Print('Hello, World!')
   Hello, World!
   
   # use "end" with empty string in print statement
   print("Hello", end = ' ')
   print("World")
   Hello World
   
   # print multiple lines
   >>> print(
   ...     "I had this thing.",
   ...     "That you could type up right.",
   ...     "But it didn't sing.",
   ...     "So I said goodnight."
   ... )
   I had this thing. That you could type up right. But it didn't sing. So I said goodnight.
   ```
   
   ```
   # type() can tell you what type a value has
   >>> type(17)
   <class 'int'>
   >>> type(3.2) 
   <class 'float'>
   >>> type('Hello, World!') 
   <class 'str'>
   >>> type('17') 
   <class 'str'> 
   >>> type('3.2') 
   <class 'str'>
   ```
   ```
   # int() function can convert value to integer
   >>> int(3.2)
   3
   ```
   ```
   # round() function can round value to two decimal places
   >>> round(8.45)
   8
   ```
   ```
   # str() function can convert value to string
   >>> print('the number is : ' + str(3))
   the number is : 3
   ```
   
# 2.2 Variables

+ **variale** : a name refers to a value

+ **assignment statement** : create new variables and give them values

+ **assignment operator =**

```
# assign a string to a new variable named message
>>> message = 'And now for something completely different' 
# assign the integer 17 to n
>>> n = 17
# assign the approximate value of π to pi
>>> pi = 3.1415926535897931

>>> print(n)
17
>>> print(pi) 3.141592653589793

>>> type(message) 
<class 'str'>
>>> type(n) 
<class 'int'>
>>> type(pi) 
<class 'float'>
```

# 2.3 Variable names and keywords

+ **variable names**
   + can contain both letters and numbers
   + can't start with a number
   + can contain a uppercase letters
   + it is better to begin with a lowercase letter 
   + can contain the underscore character ( _ ) 
   + avoid starting with an underscore character unless we are writing library code for others to use
   + can't use Python keywords
   + case sensitive
+ **Python reserves 35 keywords**
   + and as assert break class continue def 
   + del elif else except False finally for 
   + from global if import in is lambda 
   + None nonlocal not or pass raise return
   + True try while with yield async await
   
# 2.4 Statements

+ **statement**: a unit of code that the Python interpreter can execute

+ A script usually contains a sequence of statements. If there is more than one statement, the results appear one at a time as the statements execute.

```
print(1) 
x=2 
print(x)

1
2
```

# 2.5 Operators and operands

+ **operators** : + addition, - subtraction, * multiplication, / division and ** exponentiation
+ **operands** : the values the operator is applied to

```
# the division result is a floating point
>>> division = 7 / 3
>>> print(division)
2.3333333333333335

# floored (// integer) division
>>> quotient = 7 // 3
>>> print(quotient)
2

#
>>> remainder = 7 % 3
>>> print(remainder)
1
```

# 2.6 Expressions

+ **expression** : a combination of values, variables, and operators

   
# 2.7 Order of operations

+ **PEMDAS** : parentheses, exponents, multiplication, division, addtion, subtraction
   + **Parentheses** have the highest precedence
   + **Exponentiation** has the next highest precedence
   + **Multiplication** and **Division** have the same precedence, higher than **Addition** and **Subtraction**
   + Operators with the same precedence are evaluated from left to right
   
# 2.8 Modulus operator

+ **modulus operator** : 
   + works on **integers** and yields the **remainder** when the first operand is divided by the second.
   + a percent sign (%) 
   
```
# the division result is a floating point
>>> division = 7 / 3
>>> print(division)
2.3333333333333335

# floored (// integer) division
>>> quotient = 7 // 3
>>> print(quotient)
2

#
>>> remainder = 7 % 3
>>> print(remainder)
1

# So 7 divided by 3 is 2 with 1 left over.
```
+ check whether one number is divisible by another
   + if x % y is zero, then x is divisible by y
+ extract the right-most digit or digits from a number
   + x % 10 yields the right-most digit of x (in base 10)
   + x % 100 yields the last two digits
   
# 2.9 String operations

+ The **+ operator** works with strings and performs concatenation
+ **concatenation** : join the strings by linking them end to end

```
>>> first = 10
>>> second = 15
>>> print(first+second) 
25
>>> first = '100'
>>> second = '150'
>>> print(first + second) 
100150
```

+ the * operator also works with strings by multiplying the content of a string by an integer.

```
>>> first = 'Test'
>>> second = 3
>>> print(first * second)
Test Test Test
```

# 2.10 Asking the user for input

* input() function
* press Return or Enter, the program resumes and input returns

```
>>> inp = input() 
Some silly stuff 
>>> print(inp) 
Some silly stuff
```
* print a prompt telling teh user what to input

```
>>> name = input('What is your name?\n') 
What is your name?
Chuck
>>> print(name)
Chuck
```
* **sequence \n** at the end of the prompt represents a **newline**, which is a special character that causes a line break.

```
>>> name = input('What is your name?')
What is your name?Chuck
>>> print(name)
Chuck
```
```
>>> prompt = 'What...is the airspeed velocity of an unladen swallow?\n' 
>>> speed = input(prompt)
What...is the airspeed velocity of an unladen swallow?
17
>>> int(speed)
17
>>> int(speed) + 5
22
```

# 2.11 Comments

* add notes to your programs to explain in natural language what the program is doing
* start with the **# symbol**
* can put comments on a line by itself
* can put comments at the end of a line
* it has no effect on the program

# 2.12 Choosing mnemonic variable names

# 2.13 Debugging

# 2.14 Glossary
