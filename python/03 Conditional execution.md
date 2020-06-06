# Chapter 3 Conditional execution 

## 3.1 Boolean expressions

* **Boolean expression: either true or false**

```python
>>> 5 == 5 
True
>>> 5 == 6 
False
```
* **True and False belong to the class bool**

```python
>>> type(True) 
<class 'bool'> 
>>> type(False) 
<class 'bool'>
```
* **comparison operators**: compare two operands and produce True if they are equal and False otherwise

   * x==y ------ x is equal to y
   * x!=y------ x is not equal to y
   * x>y ------ x is greater than y
   * x<y ------  x is less than y
   * x>=y ------  x is greater than or equal to y
   * x<=y  ------  x is less than or equeal to y
   * x is y ------  x is the same as y
   * x is not y ------ x is not the same as y
   
## 3.2 Logical operators

* **logical operators : and, or and not**
   * and : both are true
   * or : either is true
   * not : false
   
* **any nonzero number is interpreted as "true"**

```
>>> 17 and True
True
```

# 3.3 Conditional execution

* **Conditional statements**: check conditions and change the behavior of the program accordingly

   * if it is true, thestatement gets executed.
   * if it is false, the statement is skipped.

* **if statement**

   * head line
      * start with if
      * condition : the boolean expression after the if statement
      * end with a colon character (:) 
   * body
      * indented block : the line(s) after the if statement
      * the number of statements : no limit, at least one
      * pass statement: no statement, as a place holder, does nothing
   
```python
# syntax of the if statement
if x > 0 :
    print('x is positive')
```

```python
# pass statement
if x < 0:
    pass     # need to handle nagetive values!
```
* **If you enter an if statement in the Python interpreter...**

   * the prompt change from three chevrons (<<<) to three dots (...)
      * indicate you are in the middle of a block of statements
      
   * leave a blank line at the end of a block, otherwise Python will return an error.
   
```python
>>> x = 3
>>> if x < 10:
...    print('Small') 
...
Small
>>>
```
```python
>>> x = 12
>>> if x < 10 :
...    print('Small')
... 
>>> 
```
   
# 3.4 Alternative execution

* **Alternative execution**: there are two possibilities and the condition determines which one gets executed
* **if statement**: if...else...
* **branches**: the alternatives

```
# syntax of the if statement for alternative execution
if x%2 == 0 :
   print('x is even')
else :
   print('x is odd')
```

# 3.5 Chained conditionals

* **Chained conditionals**: there are more than two possibilities
* **if statement**: if...elif(else if)...else...
   * no limit on the number of elif statements
   * else clause is at the end, but there doesn't have to be done.

```
if x < y:
   print('x is less than y')
elif x > y:
   print('x is greater than y')
else:
   print('x and y are equal')
```

* Each condition is checked in order. If the first is false, the next is checked, and so on. If one of them is true, the corresponding branch executes, and the statement ends. Even if more than one condition is true, only the first true branch executes.

# 3.6 Nested conditionals

```
if x == y:
   print('x and y are equal')
else:
   if x < y:
      print('x is less than y') 
   else:
      print('x is greater than y')
```

# 3.7 Catching exceptions using try and except

* Handling an exception with a try statement is called catching an exception.

```
inp = input('Enter Fahrenheit Temperature:') 
try:
   fahr = float(inp)
   cel = (fahr - 32.0) * 5.0 / 9.0 
   print(cel)
except:
   print('Please enter a number')
```
* Python starts by executing the sequence of statements in the try block. 
* If all goes well, it skips the except block and proceeds. 
* If an exception occurs in the try block, Python jumps out of the try block and executes the sequence of statements in the except block.

# 3.8 Short-circuit evaluation of logical expressions

* short-circuit rule

When Python detects that there is nothing to be gained by evaluating the rest of a logical expression, it stops its evaluation and does not do the computations in the rest of the logical expression. 

* guardian pattern : a guard evaluation

# 3.9 Debugging

* what kind of error it was
   * syntax errors
   * whitespace errors
   
* where it occurred
   * error messages indicate where the problem was discovered, but that is often not where it was caused.
   * the actual error might be earlier in the code, sometimes on a previous line.

# 3.10 Glossary

* **body** 
   * The sequence of statements within a compound statement.
   
* **boolean expression** 
   * An expression whose value is either True or False. 
   
* **branch** 
   * One of the alternative sequences of statements in a conditional statement.
   
* **chained conditional** 
   * A conditional statement with a series of alternative branches.
   
* **comparison operator** 
   * One of the operators that compares its operands: ==, !=, >, <, >=, and <=.
   
* **conditional statement** 
   * A statement that controls the flow of execution depending on some condition.
   
* **condition** 
   * The boolean expression in a conditional statement that determines which branch is executed.
   
* **compound statement** 
   * A statement that consists of a header and a body. The header ends with a colon (:). The body is indented relative to the header.
   
* **guardian pattern** 
   * Where we construct a logical expression with additional comparisons to take advantage of the short-circuit behavior.
   
* **logical operator** 
   * One of the operators that combines boolean expressions: and, or, and not.
   
* **nested conditional** 
   * A conditional statement that appears in one of the branches of another conditional statement.
   
* **traceback** 
   * A list of the functions that are executing, printed when an exception occurs.
   
* **short circuit** 
   * When Python is part-way through evaluating a logical expression and stops the evaluation because Python knows the final value for the expression without needing to evaluate the rest of the expression.


 


