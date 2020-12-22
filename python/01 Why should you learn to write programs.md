Chapter 1  Why should you learn to write programs?
===========


1.1 Creativity and motivation
----------

1.2 Computer hardwarre architecture
------------

* **Central Processing Unit (CPU)**

   * CPU does the thinking and runs the program
   * very fast
   
* **Main Memory**

   * fast small temporary storage
   * fast as the CPU
   * lost on reboot
   
* **Secondary Memory**

   * slower large permanent storage
   * slower than the main memory
   * lasts until deleted
   * disk drives, flash memory, memory stick

* **Input and Output Devices**

   * Input: keyboard, mouse, touchpad
   * Output: screen, speakers, printer, DVD burner
   
* **Network Connection**

   * retrieve information over a network
   * a slower and at times unreliable form of secondary memory.


1.3 Understanding programming
--------

* **Know the programming language (Python)**

   * know the vocabulary and the grammar
   * spell the words and construct sentences

* **Tell a story**


1.4 Words and sentences
---------

* **reserved words** - very special meaning to Python

~~~
and      as        assert      break     class     continue
def      del       elif        else      expect    finally
for      from      global      if        import    in
is       lambda    nonlocal    not       or        pass
raise    return    try         while     with      yield
~~~

* **variables** - having meaning to you

   * can't use any of Python's reserved words
   
   
**function** `print`

* `print('Hello world!')`

   * enclosed in quotes, single quotes or double quotes
      * print('Hello world!') or print("Hello world!")
   * most people use single quotes
   * use double quotes when apostrophe appears in the string
      * print("It's a dog.")
      
      
1.5 Conversing with Python
-----------

## start python

* Open your **terminal** 
   * The "$" is the operating system prompt
   
* Type **Python3** and press **enter**

* Execute **Python interpreter** in **interactive mode**.
   * The `>>>` prompt showed up
   * pype python commands after >>> prompt
   
~~~python
liufangdeMacBook-Pro:~ FangLiu$ python3
Python 3.8.1 (v3.8.1:1b293b6006, Dec 18 2019, 14:08:53) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
~~~


## end python

* quit()

* exit()

* CTRL-Z
   
* CTRL-D


1.6 Terminology: Interpreter and compiler
-----------

* **high-level language** 

   * Python is a high-level language intended to be relatively straightforward for humans to read and write and for computers to read and process.
   * include python, Java, C++, PHP, Ruby, Basic, Perl, JavaScript, and many more

* **machine language**
   * a language the CPU can understand, it's hard to understand and write for human
   * represented all in zeros and ones
   * its syntax is more complex
   * It is tied to the computer hardware, not portable across different types of hardware.
   
* **translators** : convert high-level language (programs) to machine language.
  
   * **interpreter**
   
      * read the source code of the program, parse the source code and interpret the instructions on the fly   
      
      * Python interpreter is written in a high-level language called "C".
   
   * **compiler**
   
      * hand the entire program in a file
      * run a process to translate the high-level source code into machine language
      * put the resulting machine language into a file for later execution
      
      
1.7 Writing a program
--------

* use a **text editor** to write the Python instructions into a file

* program file is called a **script**, name end with **.py**

* start python in a command window, type `python hello.py`. There is no need to have quit() at the end of the Python program in the file

```
$ python hello.py
Hello world!
```


1.8 What is a program?
-----------

* program : a sequence of Python statements that have been crafted to do something


1.9 The building blocks of programs
-------------

* **input** 
   * Get data from the “outside world”. 
   * This might be reading data from a file, or even some kind of sensor like a microphone, GPS, or keyboard.

* **output** 
   * Display the results of the program on a screen or store them in a file or perhaps write them to a device like a speaker to play music or speak text.

* **sequential execution** 
   * Perform statements one after another in the order they are encountered in the script.

* **conditional execution** 
   * Check for certain conditions and then execute or skip a sequence of statements.

* **repeated execution** 
   * Perform some set of statements repeatedly, usually with some variation.

* **reuse** 
   * Write a set of instructions once and give them a name
   * reuse those instructions as needed throughout your program.


1.10 What could possibly go wrong?
---------

* **syntax errors**: 

A syntax error means that you have violated the “grammar” rules of Python. Python does its best to point right at the line and character where it noticed it was confused.   

* **logic errors**

A logic error is when your program has good syntax but there is a mistake in the order of the statements or perhaps a mistake in how the statements relate to one another.  

* **semantic errors**

A semantic error is when your description of the steps to take is syntactically perfect and in the right order, but there is simply a mistake in the program.   
   

1.11 Debugging
-------------

* **reading** 
   * examine, read and check your code
   
* **running**

* **ruminating**

* **retreating**


1.12 The learning journey
----------




1.13 Glossary
----------

* **bug**
   * An error in a program.
   
* **central processing unit**
   * The heart of any computer. It is what runs the software that we write; also called “CPU” or “the processor”.
   
* **compile**
   * To translate a program written in a high-level language into a low-level language all at once, in preparation for later execution.
   
* **high-level language**
   * A programming language like Python that is designed to be easy for humans to read and write.
   
* **interactive mode**
   * A way of using the Python interpreter by typing commands and expressions at the prompt.
   
* **interpret**
   * To execute a program in a high-level language by translating it one line at a time.
   
* **low-level language**
   * A programming language that is designed to be easy for a computer to execute; also called “machine code” or “assembly language”.
   
* **machine code**
   * The lowest-level language for software, which is the language that is directly executed by the central processing unit (CPU).
   
* **main memory**
   * Stores programs and data. Main memory loses its information when the power is turned off.
   
* **parse**
   * To examine a program and analyze the syntactic structure.
   
* **portability**
   * A property of a program that can run on more than one kind of computer.
   
* **print function**
   * An instruction that causes the Python interpreter to display a value on the screen.
   
* **problem solving**
   * The process of formulating a problem, finding a solution, and expressing the solution.
   
* **program**
   * A set of instructions that specifies a computation.
   
* **prompt**
   * When a program displays a message and pauses for the user to type some input to the program.
   
* **secondary memory**
   * Stores programs and data and retains its information even when the power is turned off. Generally slower than main memory. Examples of secondary memory include disk drives and flash memory in USB sticks. 
   
* **semantics**
   * The meaning of a program.
   
* **semantic error**
   * An error in a program that makes it do something other than what the programmer intended.
   
* **source code**
   * A program in a high-level language.


1.14 Exercises
---------------

**Exercise 1: What is the function of the secondary memory in a computer?**  
a) Execute all of the computation and logic of the program  
b) Retrieve web pages over the Internet  
c) Store information for the long term, even beyond a power cycle  
d) Take input from the user  

**Answer:**  
C


**Exercise 2: What is a program?**

**Answer:**   
A program is a sequence of Python statements that have been crafted to do something.


**Exercise 3: What is the difference between a compiler and an interpreter?**  

**Answer:**   
An interpreter reads the source code of the program as written by the programmer, parses the source code, and interprets the instructions on the fly.
A compiler needs to be handed the entire program in a file, and then it runs a process to translate the high-level source code into machine language and then the compiler puts the rusulting machine language into a file for later execution.


**Exercise 4: Which of the following contains “machine code”?**  
a) The Python interpreter  
b) The keyboard  
c) Python source file  
d) A word processing document  

**Answer:**  
A


**Exercise 5: What is wrong with the following code:**

```python
>>> primt 'Hello world!'  
File "<stdin>", line 1  
	primt 'Hello world!'  
                           ^
SyntaxError: invalid syntax
>>>
```
**Answer:**
The function print() wasn't writen correctly. It was written by "Primt". The print statement should enclosed in quotes and in parentheses. print('Hello world!')

  
**Exercise 6: Where in the computer is a variable such as “x” stored after the following Python line finishes?**

x = 123

a) Central processing unit  
b) Main Memory  
c) Secondary Memory  
d) Input Devices  
e) Output Devices  

**Answer:**  
B


**Exercise 7: What will the following program print out:**  

x = 43  
x=x+1  
print(x)   

a) 43  
b) 44  
c) x + 1  
d) Error because x = x + 1 is not possible mathematically  

**Answer: B**

**Exercise 8: Explain each of the following using an example of a human capability: (1) Central processing unit, (2) Main Memory, (3) Secondary Memory, (4) Input Device, and (5) Output Device. For example, “What is the human equivalent to a Central Processing Unit”?**

**Answer:**
(1) Central processing unit likes human brain; (2) Main Memory likes our short-term memory; (3) Secondary Memory likes our long-term memory; (4) Input Device likes our ears when listening and (5) Output Device likes our mouth when speaking


**Exercise 9: How do you fix a “Syntax Error”?**\

**Answer:**  
Examine your code, read it back to yourself, and check that it says what you meant to say. Check your python grammer.


----------


* comma-separated sequence print with space between

```
>>> print("Hello","World!")
Hello World!
>>> print("Hello""World")
HelloWorld
>>> print(1,000,000)
1 0 0
```

* print in one line

   * put **end=' '** at the end of print line to tell us not end the line with a newline character and go to the next line.

```
print("Hello", end = ' ')
print("World")
Hello World
```
   * print multiple lines, each line end with ","

```
>>> print(
...     "I had this thing.",
...     "That you could type up right.",
...     "But it didn't sing.",
...     "So I said goodnight."
... )
I had this thing. That you could type up right. But it didn't sing. So I said goodnight.
```

* newline character

   * \n (backslash n): start a new line, cause a line break
   
```
>>> days = "\nMon\nTue\nWed\nThu\nFri\nSat\nSun"
>>> print("Here are the days: ", days)
Here are the days:  
Mon
Tue
Wed
Thu
Fri
Sat
Sun
```

   * three double-quotes(triple-quotes, """): start a new line
   
```
>>> days = """
... Mon
... Tue
... Wed
... """
>>> print("Here are the days: ", days)
Here are the days:  
Mon
Tue
Wed
```

* escape sequences
   
Escape | What it does
|:---|:---|
\\ | Backslash (\)
\' | Single-quote (')
\" | Double-quote (")   
\a | ASCII bell (BEL)
\b | ASCII backspace (BS)
\f | ASCII formfeed (FF)
\n | ASCII linefeed (LF)
\N{name} | Character named name in the Unicode database (Unicode only) 
\r | ASCII carriage return (CR)
\t | ASCII horizontal tab (TAB)
\uxxxx | Character with 16-bit hex value xxxx (Unicode only) 
\Uxxxxxxxx | Character with 32-bit hex value xxxxxxxx (Unicode  only) 
\v | ASCII vertical tab (VT)
\ooo | Character with octal value oo
\xhh | Character with hex value hh
   
```
>>> print("I am 6'2\" tall.")
I am 6'2" tall.
```
