# Chapter 5  Iteration

## 5.1 Updating variables

* **initialize** - assign a variable

* **update** - reassign a variable
   * **increment** : by adding 1
   * **decrement** : by subtracting 1

```python
>>> x = 0     # initialize
>>> x = x + 1    # updating by increment
```

## 5.2 The `while` statement

* **`while` statement** - one form of iteration

```python
n = 5
while n > 0:
    print(n)
    n = n - 1 
print('Blastoff!')
```
* **the flow of execution for a while statement**
   * evaluate the condition, yielding True or False
      * False: exit the while statement and continue execution at the next statement
      * True: execute the body and then go back to step 1
      
* **loop** - this type of flow
   * iteration：each time we execute the body of the loop
   * iteration variable: change each time through a loop

## 5.3 Infinite loops 

### Ending infinite loop with `break`

* **infinite loop**: there is no iteration variable telling you how many times to execute the loop

```python
n = 10 
while True:
    print(n, end=' ')
    n=n-1 
print('Done!')
```
* **`break` statement**: to exit the loop when we have reached the exit condition**

```python
while True:
    line = input('> ') 
    if line == 'done':
        break
    print(line)
print('Done!')

> hello there
hello there
> finished
finished
> done Done!
```

### Finishing iterations with `continue`

* **continue statement: to end the current iteration and jump back to the while statement to start the next iteration

```python
while True:
    line = input('> ') 
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

> hello there
hello there
> # don't print this
> print this!
print this!
> done
Done!
```

## 5.4 Definite loops using `for`

* **`for` loop** - to construct a definite loop

   * **`for` statement**
      * iteration variable: friend
   * **loop body**

```python
for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff!')

5
4
3
2
1
Blastoff!
```

```python
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')

Happy New Year: Joseph
Happy New Year: Glenn
Happy New Year: Sally
Done!
```

## 5.6 Loop patterns

These loops are generally constructed by:  

* Initializing one or more variables before the loop starts

* Performing some computation on each item in the loop body, possibly changing the variables in the body of the loop

* Looking at the resulting variables when the loop completes

 ### 5.6.1 Counting and summing loops
 
 * counting loop: count the number of items in a list
    * built-in function len()
 
 ```python
 count = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    count = count + 1
print('Count: ', count)

Count: 6
```

* summing loop: compute the total of a set of numbers
   * built-in function sum()

```python
total = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    total = total + itervar
print('Total: ', total)

Total: 154
```

### 5.6.2 Maximum and minimum loops

* Maxium loop: find the largest value in a list or sequence
   * built-in function max()

```python
largest = None
print('Before:', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest :
        largest = itervar
    print('Loop:', itervar, largest)
print('Largest:', largest)

Before: None
Loop: 3 3
Loop: 41 41
Loop: 12 41
Loop: 9 41
Loop: 74 74
Loop: 15 74
```
* Minium loop: find the smallest value in a list or sequence
   * built-in function min()

# 5.7 Debugging

* the mid-point check


## 5.8 Glossary

* **accumulator** A variable used in a loop to add up or accumulate a result. 

* **counter** A variable used in a loop to count the number of times something hap- pened. We initialize a counter to zero and then increment the counter each time we want to “count” something.

* **decrement** An update that decreases the value of a variable.

* **initialize** An assignment that gives an initial value to a variable that will be updated.

* **increment** An update that increases the value of a variable (often by one). 

* **infinite loop** A loop in which the terminating condition is never satisfied or for which there is no terminating condition.

* **iteration** Repeated execution of a set of statements using either a function that
calls itself or a loop.

## 5.9 Exercises 

**Exercise 1: Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.**

Enter a number: 4  
Enter a number: 5  
Enter a number: bad data    
Invalid input  
Enter a number: 7  
Enter a number: done  
16 3 5.333333333333333  

**Answer:**

```python
count = 0
total = 0
average = 0

while True:
    number = input("Enter a number: ")
    try:
        value = float(number)
        count = count + 1
        total = total + value
        average = total / count
    except:
        if number == "done":
            break
        else:
            print("Invalid Input")
            continue
print(total, count, average)
```
```python
total = 0
count = 0
average = 0

while True:
    try:
        number = input("Enter a number: ")
        if (number == 'done'):
            break
        value = float(number)
        total = value + total
        count = count + 1
        average = total / count
    except:
        print('Invalid input')
print(total, count, average)
```

**Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.**

**Answer:**

```python
count = 0
total = 0
average = 0
largest = None
smallest = None

while True:
    number = input("Enter a number: ")
    try:
        number = float(number)
        count = count + 1
        total = total + number
        average = total / count
        if smallest is None or number < smallest:
            smallest = number
        if largest is None or number > largest:
            largest = number
    except:
        if number == 'done':
            break
        else:
            print('Invalid Input')
            continue
print(count, largest, smallest)
```
```python
count = 0
total = 0
average = 0
list = [ ]

while True:
    number = input("Enter a number: ")
    if (number == 'done'):
        break
    number = float(number)
    total = total + number
    count = count + 1
    average = total / count
    list.append(number)

print(average, max(list), min(list))
```
