# 3.1 Boolean expressions
* either true or false
* operator == compare two operands and produce True if they are equal and False otherwise
```
>>> 5 == 5 
True
>>> 5 == 6 
False
```
* True and False belong to the **class bool**
```
>>> type(True) 
<class 'bool'> 
>>> type(False) 
<class 'bool'>
```
* comparison operators
   * x==y ------ x is equal to y
   * x!=y------ x is not equal to y
   * x>y ------ x is greater than y
   * x<y ------  x is less than y
   * x>=y ------  x is greater than or equal to y
   * x<=y  ------  x is less than or equeal to y
   * x is y ------  x is the same as y
   * x is not y ------ x is not the same as y
   
# 3.2 Logical operators

* logical operators : and, or and not
   * and : both are true
   * or : either is true
   * not : 
* any nonzero number is interpreted as "true"

```
>>> 17 and True
True
```

# 3.3 Conditional execution

* **if statement**

   * the condition : the boolean expression after the if statement
   * if statement : end with a colon character (:)
   * the line(s) after the if statement are indented
   
```
if x > 0 :
    print('x is positive')
```

   * if the logical condition is true, indented statement gets executed.
   * if the logical condition is false, indented statement is skipped.
   
```
>>> x = 3
>>> if x < 10:
...    print('Small') 
...
Small
>>>
```
```
>>> x = 12
>>> if x < 10 :
...    print('Small')
... 
>>> 
```
* the prompt change from three chevrons (<<<) to three dots (...) to indicate you are in the middle of a block of statements
* leave a blank line at the end of a block, otherwise Python will return an error.

* pass statement
   * have a body with no statement
   * as a place holder for code you haven't written yet

```
if x < 0 :
   pass     # need to handle negative values!
```
   
   
# 3.4 Alternative execution

* if statement
* there are two possibilities and the condition determines which one gets executed
* branches

```
if x%2 == 0 :
   print('x is even')
else :
   print('x is odd')
```

# 3.5 Chained conditionals

* there are more than two possibilities
* elif is an abbreviation of "else if"
* there is no limit on the number of elif statements
* else clause is at the end, but there doesn't have to be done.

```
if x < y:
   print('x is less than y')
elif x > y:
   print('x is greater than y')
else:
   print('x and y are equal')
```

* Each condition is checked in order. 
* If the first is false, the next is checked, and so on. 
* If one of them is true, the corresponding branch executes, and the statement ends. 
* Even if more than one condition is true, only the first true branch executes.

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
* a guard

# 3.9 Debugging

* what kind of error it was
   * syntax errors
   * whitespace errors
   
* where it occurred
   * error messages indicate where the problem was discovered, but that is often not where it was caused.
   * the actual error might be earlier in the code, sometimes on a previous line.

# 3.10 Glossary

* **body** The sequence of statements within a compound statement.
* **boolean expression** An expression whose value is either True or False. 
* **branch** One of the alternative sequences of statements in a conditional statement.
* **chained conditional** A conditional statement with a series of alternative branches.
* **comparison operator** One of the operators that compares its operands: ==, !=, >, <, >=, and <=.
* **conditional statement** A statement that controls the flow of execution depend- ing on some condition.
* **condition** The boolean expression in a conditional statement that determines which branch is executed.
* **compound statement** A statement that consists of a header and a body. The header ends with a colon (:). The body is indented relative to the header.
* **guardian pattern** Where we construct a logical expression with additional com- parisons to take advantage of the short-circuit behavior.
* **logical operator** One of the operators that combines boolean expressions: and, or, and not.
* **nested conditional** A conditional statement that appears in one of the branches of another conditional statement.
* **traceback** A list of the functions that are executing, printed when an exception occurs.
* **short circuit** When Python is part-way through evaluating a logical expression and stops the evaluation because Python knows the final value for the ex- pression without needing to evaluate the rest of the expression.


 


