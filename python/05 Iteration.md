# 5.1 Updating variables

* **initialize** a variable
* **update** a variable
   * **increment** : updating a variable by adding 1
   * **decrement** : updating a variable by subtracting 1

```
>>> x = 0
>>> x = x + 1
```

# 5.2 The while statement

* **while** statement

```
n=5
while n > 0:
    print(n)
    n=n-1 
print('Blastoff!')
```
* the flow of execution for a while statement
   * evaluate the condition, yielding True or False
      * False: exit the while statement and continue execution at the next statement
      * True: execute the body and then go back to step 1
* loop
* iteration
* iteration variable
* infinite loop : there is no iteration variable, the loop will repeat forever

# 5.3 Infinite loops

* infinite loop: there is no iteration variable telling you how many times to execute the loop

```
n = 10 
while True:
    print(n, end=' ')
    n=n-1 
print('Done!')
```
* break statement 
```
while True:
    line = input('> ') 
    if line == 'done':
        break
    print(line)
print('Done!')
```




# 5.4 Finishing iterations with continue

```
while True:
    line = input('> ') 
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')
```

# 5.5 Definite loops using for



# 5.6 Loop patterns



# 5.7 Debugging



# 5.8 Glossary

* **accumulator** A variable used in a loop to add up or accumulate a result. 

* **counter** A variable used in a loop to count the number of times something hap- pened. We initialize a counter to zero and then increment the counter each time we want to “count” something.

* **decrement** An update that decreases the value of a variable.

* **initialize** An assignment that gives an initial value to a variable that will be updated.

* **increment** An update that increases the value of a variable (often by one). 

* **infinite loop** A loop in which the terminating condition is never satisfied or for which there is no terminating condition.

* **iteration** Repeated execution of a set of statements using either a function that
calls itself or a loop.
