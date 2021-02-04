# Chapter 7  Files

## 7.1 File Processing

* A text file can be thought of as a sequence of lines

## 7.2 Opening files

* **`open()` function**

   * find the file by name and make sure the file exists.
   
   * returns a "file handle" - a variable used to perform operations(open/read/write/close) on the file
   
* **handle = open(filename, mode)**

   * **handle** - use to manipulate the file, open-read-write-close
   * **filename** is a string
   * **mode** is optional
      * 'r' -  we are planning to read the file
      * 'w' -  we are going to write to the file

```python
>>> fhand = open('mbox.txt')
>>> print(fhand)
<_io.TextIOWrapper name='mbox.txt' mode='r' encoding='UTF-8'>

>>> fhand = open('mbox.txt', 'r')     # mode: read
>>> print(fhand)
<_io.TextIOWrapper name='mbox.txt' mode='r' encoding='UTF-8'>

>>> fhand = open('mbox.txt', 'w')     # mode: write
>>> print(fhand)
<_io.TextIOWrapper name='mbox.txt' mode='w' encoding='UTF-8'>

# If the file does not exist, open will fail with a traceback
>>> fhand = open('stuff.txt')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'stuff.txt'
```

## 7.3 Text files and lines

* **newline character** - represents the end of the line, separates the characters in the file into lines
   * backslash-n (`\n`)
   * a single character (not two)
   * escape, non-printable character
   * every line is ended by a newline
   
```python
>>> stuff = 'Hello\nWorld!' 
>>> stuff
'Hello\nWorld!'
>>> print(stuff)
Hello
World!
>>> stuff = 'X\nY'
>>> print(stuff)
X
Y
>>> len(stuff)
3
```

## 7.4 Reading files

* **Counting lines in a file** - `for` loop counting pattern

```python
>>> fhand = open('mbox.txt')         # open a file read-only
>>> count = 0
>>> for line in fhand:               # use a for loop to read each line
...     count = count + 1            # count the lines and print out the numbers of lines
... 
>>> print('Line Count:', count)
Line Count: 132045
```

* **`read()` method : read the whole file into one string**

```python
>>> fhand = open('mbox.txt')
>>> inp = fhand.read()
>>> print(len(inp))
6687002
>>> print(inp[:20])
From stephen.marquar

# store the output of read as a variable because each call to read exhausts the resource
>>> fhand = open('test.txt')
>>> print(len(fhand.read()))
31
>>> print(len(fhand.read()))
0
```

## 7.5 Searching through a file

* We put an `if` statement in `for` loop to print lines that meet some criteria

* **`startswith()` method** : select the lines with the desired prefix

```python
>>> fhand = open('mbox-short.txt')
>>> for line in fhand:
...     if line.startswith('From:'):
...         print(line)
... 
From: stephen.marquard@uct.ac.za

From: louis@media.berkeley.edu

From: zqian@umich.edu

From: rjlowe@iupui.edu
...

```

* The output has the extra blank lines, because of the invisible newline character.

* **`rstrip()` method** : strip whitespace from the right side of a string

```python
>>> fhand = open('mbox-short.txt')
>>> for line in fhand:
...     line = line.rstrip()
...     if line.startswith('From:'):
...         print(line)
... 
From: stephen.marquard@uct.ac.za
From: louis@media.berkeley.edu
From: zqian@umich.edu
From: rjlowe@iupui.edu
...

```

* **Skipping with `continue`**

```python
>>> fhand = open('mbox-short.txt')
>>> for line in fhand:
...     line = line.rstrip()
...     if not line.startswith('From:'):    # skip all lines not start with"From:"
...         continue
...     print(line)
... 
From: stephen.marquard@uct.ac.za
From: louis@media.berkeley.edu
From: zqian@umich.edu
From: rjlowe@iupui.edu
...
```

```python
>>> fhand = open('mbox-short.txt')
>>> for line in fhand:
...     line = line.rstrip()
...     if line.find('@uct.ac.za') == -1:    # the string was not found; skipped
...         continue
...     print(line)
... 
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to stephen.marquard@uct.ac.za using -f
From: stephen.marquard@uct.ac.za
Author: stephen.marquard@uct.ac.za
...
```

* **Using `in` to select lines**

```pyhton
>>> fhand = open('mbox-short.txt')
>>> for line in fhand:
...     line = line.rstrip()
...     if not '@uct.ac.za' in line:         # skip all lines not include '@uct.ac.za'
...         continue
...     print(line)
... 
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to stephen.marquard@uct.ac.za using -f
From: stephen.marquard@uct.ac.za
Author: stephen.marquard@uct.ac.za
```


## 7.6 Letting the user choose the file name

* use `input()` to read the file name

```python
fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)

python3 inp_file.py
Enter the file name: mbox.txt
There were 1797 subject lines in mbox.txt

python3 inp_file.py
Enter the file name: mbox-short.txt
There were 27 subject lines in mbox-short.txt
```

## 7.7 Using try, except, and open

* **try/except structure**

```python
fname = input('Enter the file name: ') 
try:
    fhand = open(fname) 
except:
    print('File cannot be opened:', fname)
    quit()    
    # same as exit()
    
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)

python3 try_file.py
Enter the file name: mbox.txt
There were 1797 subject lines in mbox.txt

# bad file names
python3 try_file.py
Enter the file name: na na boo boo        
File cannot be opened: na na boo boo
```

## 7.8 Writing files

* **write mode** : open it with mode "w" as a second paremeter
   * file exist : clear out the old data and start fresh
   * file doesn't exist : create a new file

```python
>>> fout = open('test.txt', 'w')
>>> print(fout)
<_io.TextIOWrapper name='test.txt' mode='w' encoding='UTF-8'>
```

* **`write` method**
   * `file.write()`: put data into the file, return the number of characters written.
   * `file.close()`: close the file to make sure that the data is written to the disk
   
```python
>>> line1 = "This here's the wattle,\n" 
>>> fout.write(line1)
24
>>> line2 = 'the emblem of our land.\n' 
>>> fout.write(line2)
24
>>> fout.close()
```


# 7.9 Debugging

* built-in function `repr()` : take any object as an argument and returns a string representation of the object.
   * represent whitespace characters with backslash sequences
   
```python
>>> s = '1 2\t 3\n 4' 
>>> print(s)
1 2  3
 4
>>> print(repr(s)) 
'1 2\t 3\n 4'
````

# 7.10 Glossary

* **catch** To prevent an exception from terminating a program using the try and except statements.
* **newline** A special character used in files and strings to indicate the end of a line.
* **Pythonic** A technique that works elegantly in Python. “Using try and except is the Pythonic way to recover from missing files”.
* **Quality Assurance** A person or team focused on insuring the overall quality of a software product. QA is often involved in testing a product and identifying problems before the product is released.
* **text file** A sequence of characters stored in permanent storage like a hard drive.

## 7.11 Exercises

**Exercise 1: Write a program to read through a file and print the contents of the file (line by line) all in upper case. Executing the program will look as follows:**

python shout.py
Enter a file name: mbox-short.txt
FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN 5 09:14:16 2008 
RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG> 
RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
     BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA; 
     SAT, 05 JAN 2008 09:14:16 -0500

**Answer:**

```python
fname = input('Enter a file name: ')
fhand = open(fname)

for line in fhand:
    line = line.rstrip()
    print(line.upper())
```


**Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form:**

X-DSPAM-Confidence: 0.8475

When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point number on the line. Count these lines and then compute the total of the spam confidence values from these lines. When you reach the end of the file, print out the average spam confidence.

Enter the file name: mbox.txt
Average spam confidence: 0.894128046745

Enter the file name: mbox-short.txt 
Average spam confidence: 0.750718518519

Test your file on the mbox.txt and mbox-short.txt files.

```python
fname = input('Enter the file name: ')
fhand = open(fname)

count = 0
sum = 0

for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        atpos = line.find(':')
        data = float(line[atpos+2:])
        count = count + 1
        sum = sum + data
        average = sum / count

print('Average spam confidence:', average)
```

**Exercise 3: Sometimes when programmers get bored or want to have a bit of fun, they add a harmless Easter Egg to their program. Modify the program that prompts the user for the file name so that it prints a funny message when the user types in the exact file name “na na boo boo”. The program should behave normally for all other files which exist and don’t exist. Here is a sample execution of the program:**

python egg.py
Enter the file name: mbox.txt
There were 1797 subject lines in mbox.txt

python egg.py
Enter the file name: missing.tyxt 
File cannot be opened: missing.tyxt

python egg.py
Enter the file name: na na boo boo
NA NA BOO BOO TO YOU - You have been punk'd!

We are not encouraging you to put Easter Eggs in your programs; this is just an exercise.

```python
fname = input('Enter the file name: ')

try:
    fhand = open(fname)
except:
    if fname == 'na na boo boo':
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        exit()
    else:
        print("File cannot be opened:", fname)
        exit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
```
