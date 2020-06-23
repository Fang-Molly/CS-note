# Chapter 7  Files

## 7.1 Persistence

## 7.2 Opening files

* open files : find the file by name and make sure the file exists.

* go to the same folder which the file stored in and start python

* return a file handle
   * file handle : to open/close/read/write

```
>>> fhand = open('mbox.txt')
>>> print(fhand)
<_io.TextIOWrapper name='mbox.txt' mode='r' encoding='cp1252'>
```

* If the file does not exist, open will fail with a traceback

```
>>> fhand = open('stuff.txt')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'stuff.txt'
```

## 7.3 Text files and lines

* **newline character**
   * backslash-n (\n), a single character
   
```
>>> stuff = 'X\nY'
>>> print(stuff)
X
Y
>>> len(stuff)
3
```

## 7.4 Reading files

* construct a for loop to read through and count each of the lines in a file:

```python
fhand = open('sample.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)

Line Count: 4
```

* **read method : read the whole file into one string**

```
>>> fhand = open('test.txt')
>>> inp = fhand.read()
>>> print(len(inp))
28
>>> print(inp[:20])
I love you
Hello
How
```
* store the output of read as a variable because each call to read exhausts the resource

```
>>> fhand = open('test.txt')
>>> print(len(fhand.read()))
31
>>> print(len(fhand.read()))
0
```

## 7.5 Searching through a file

* method **startswith** : select the lines with the desired prefix:

```
>>> fhand = open('test.txt')
>>> count = 0
>>> for line in fhand:
...     if line.startswith('I'):
...         print(line)
... 
I love you!

I love your shirt!
```
* The output has the extra blank lines, because of the invisible newline character.

* method **rstrip** : strip whitespace from the right side of a string

```
>>> fhand = open('test.txt')
>>> for line in fhand:
...     line = line.rstrip()
...     if line.startswith('I'):
...         print(line)
... 
I love you!
I love your shirt!
```

* **continue**



# 7.6 Letting the user choose the file name

* use input to read the file name

* 






# 7.7 Using try, except, and open

* try/except structure
* exit function terminates the program
```
fname = input('Enter the file name: ') 
try:
    fhand = open(fname) 
except:
    print('File cannot be opened:', fname)
    exit() 
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
```

# 7.8 Writing files

* write mode : open it with mode "w" as a second paremeter
   * file exist : clear out the old data and start fresh
   * file doesn't exist : create a new file

```
>>> fout = open('test.txt', 'w')
>>> print(fout)
<_io.TextIOWrapper name='test.txt' mode='w' encoding='UTF-8'>
```
* write method 
   * put data into the file, return the number of characters written.
   * fout.close(): close the file to make sure that the data is written to the disk
   
```
>>> line1 = "This here's the wattle,\n" 
>>> fout.write(line1)
24
>>> line2 = 'the emblem of our land.\n' 
>>> fout.write(line2)
24
>>> fout.close()
```


# 7.9 Debugging

* built-in function repr






# 7.10 Glossary

* **catch** To prevent an exception from terminating a program using the try and except statements.
* **newline** A special character used in files and strings to indicate the end of a line.
* **Pythonic** A technique that works elegantly in Python. “Using try and except is the Pythonic way to recover from missing files”.
* **Quality Assurance** A person or team focused on insuring the overall quality of a software product. QA is often involved in testing a product and identifying problems before the product is released.
* **text file** A sequence of characters stored in permanent storage like a hard drive.

## 7.11 Exercises

Exercise 1: Write a program to read through a file and print the contents of the file (line by line) all in upper case. Executing the program will look as follows:
python shout.py
Enter a file name: mbox-short.txt
FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN 5 09:14:16 2008 RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG> RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA; SAT, 05 JAN 2008 09:14:16 -0500
You can download the file from www.py4e.com/code3/mbox-short.txt 


Exercise 2: Write a program to prompt for a file name, and then read
through the file and look for lines of the form:
X-DSPAM-Confidence: 0.8475
When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point number on the line. Count these lines and then compute the total of the spam confidence values from these lines. When you reach the end of the file, print out the average spam confidence.

Enter the file name: mbox.txt
Average spam confidence: 0.894128046745
Enter the file name: mbox-short.txt Average spam confidence: 0.750718518519
Test your file on the mbox.txt and mbox-short.txt files.
FILES


Exercise 3: Sometimes when programmers get bored or want to have a bit of fun, they add a harmless Easter Egg to their program. Modify the program that prompts the user for the file name so that it prints a funny message when the user types in the exact file name “na na boo boo”. The program should behave normally for all other files which exist and don’t exist. Here is a sample execution of the program:
python egg.py
Enter the file name: mbox.txt
There were 1797 subject lines in mbox.txt
python egg.py
Enter the file name: missing.tyxt File cannot be opened: missing.tyxt
python egg.py
Enter the file name: na na boo boo
NA NA BOO BOO TO YOU - You have been punk'd!
We are not encouraging you to put Easter Eggs in your programs; this is just an exercise.
