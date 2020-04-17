# 1.1 Creativity and motivation

# 1.2 Computer hardwarre architecture

* **Central Processing Unit (CPU)**
   * CPU is built to be obsessed with “what is next?”
   
* **Main Memory**
   * Store information that the CPU needs in a hurry.
   * Nearly as fast as the CPU
   * The information stored in the main memory vanishes when the computer is turned off.
   
* **Secondary Memory**
   * Store information
   * Much slower than the main memory
   * It can store information even when there is no power to the computer.
   * Disk drives or flash memory 

* **Input and Output Devices**
   * screen, keyboard, mouse, microphone, speaker, touchpad, etc.
   
* **Network Connection**
   * retrieve information
   * a slower and at times unreliable form of secondary memory.

# 1.3 Understanding programming

* First, you need to know the programming language (Python) - you need to know the vocabulary and the grammar. You can spell the words and construct sentences.

* Second, you need to tell a story.

# 1.4 Words and sentences

* **reserved words**

and; as; assert; break; class; continue; def; del; elif; else; expect; inally; for; from; global; if; import; in;       
is; lambda; nonlocal; not; or; pass; raise; return; try; while; with; yield    

* **variables**

# 1.5 Conversing with Python

## start python

* Open your **terminal** 
   * The "$" is the operating system prompt
* type **Python3** and press **enter**

* execute **Python interpreter** in **interactive mode**.
   * The `>>>` prompt showed up
   * pype python commands after >>> prompt
   
```
liufangdeMacBook-Pro:~ FangLiu$ python3
Python 3.8.1 (v3.8.1:1b293b6006, Dec 18 2019, 14:08:53) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> print ('Hello world!')
Hello world!
```

## end python

* quit()

* Hit CTRL-Z(^Z)
   
* Hit CTRL-D(^D)

## **print() function**

* print( )
* enclosed in quotes, single quotes and double quotes do the same thing
   * print('Hello world!') or print("Hello world!")
* most people use single quotes
* use double quotes when apostrophe appears in the string
   * print("It's a dog.")
------------------------------------

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

* new line character

   * \n (backslash n): start a new line
   
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

# 1.6 Terminology: Interpreter and compiler

* **high-level language** 
   * it is easy to read and write for computers and human
   * include python, Java, C++, PHP, Ruby, Basic, Perl, JavaScript, and many more\
   * use for writing programs

* **machine language**
   * a language the CPU can understand, it's hard to understand and write for human
   * represented all in zeros and ones
   * its syntax is more complex
   * It is tied to the computer hardware, not portable across different types of hardware.
   
* **translators** : convert high-level language (programs) to machine language.
   * **interpreter**
      * read the source code of the program
      * parse the source code
      * interpret the instructions
      * Python interpreter is written in a high-level language called "C".
   * **compiler**
      * hand the entire program in a file
      * run a process to translate the high-level source code into machine language
      * put the resulting machine language into a file for later execution
      
# 1.7 Writing a program

* use a **text editor** to write the Python instructions into a file, which is called a **script**
* name end with **.py**

```
$ python hello.py
Hello world!
```

* There is no need to have quit() at the end of the Python program in the file

# 1.8 What is a program?

* program : a sequence of Python statements that have been crafted to do something


# 1.9 The building blocks of programs

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

# 1.10 What could possibly go wrong?

* **syntax errors**
* **logic errors**
* **semantic errors**

# 1.11 Debugging

* **debugging** 
   * the process of finding the cause of the error in your code

* **reading** 
   * examine, read and check your code
* **running**

* **ruminating**

* **retreating**

# 1.12 The learning journey


# 1.13 Glossary

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


# Summary

1. how to start and end python?
2. print( )
3. error types
