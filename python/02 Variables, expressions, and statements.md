# 2.1 Values and types
+ value: a letter or a number
+ types
   + **integer**: type ```int```; 2
   + **string**: type ```str```; enclosed in quotation marks.
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
# 2.2 Variables

+ **variale** : a name refers to a value

+ **assignment statement** : create new variables and give them values

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
   + begin with a lowercase letter


