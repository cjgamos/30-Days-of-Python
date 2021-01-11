# 🐍 30 Days Of Python

**Days**      | **Topics**    
--------------|-----------
01            | *Introduction*
02            | *Variables, Buil-in Functions*
03            | *Operators*
04            | *Strings*
05            | *Lists*
06            | *Tuples*
07            | *Sets*
08            | *Dictionaries*
09            | *Conditionals*
10            | *Loops*
11            | *Functions*
12            | *Modules*
13            | *List Comprehension*
14            | *Higher Order Functions*
15            | *Python Type Errors*
16            | *Python Date Time*
17            | *Exception Handling*
18            | *Regular Expressions*
19            | *File Handling*
20            | *Python Package Manager*
21            | *Classes and Objects*
22            | *Web Scraping*
23            | *Virtual Environment*
24            | *Statistics*
25            | *Pandas*
26            | *Python web*
27            | *Python with MongoDB*
28            | *API*
29            | *Building API*
30            | *Conclusions*

# 📘 Day 1

## Introduction

Python is a high-level programming language for general-purpose programming. This is a 30 days python challenge, in where i am going to 
challenge myself to re-learn python for a month. I am going to use Python 3. I've broken down the topics into 30 days, where each day
contains several topics, explanations, real-world examples and hands on exercises.

This is just for learning purposes repository. 

## Why Python ? 

Python was my very first language, and it is easy to learn and easy to use. It is used by various industries and companies (Google, Facebook, Instagram, Etc.).
It has been used to develop web applications, system adminstration, desktop applications, and specially machine learning and data science. It is embraced in 
Data science and Machine learning community. 

## Python

### Python Shell

Python is an interpreted scripting language, so it doesn't need to be compiled. It executes the code line by line. When you enter the code, 
it interprets the code and shows the result in the next line. Open your terminal or command prompt(cmd) and write:

```python
python
```
The python interactive shell is opened and it is waiting for you to write some codes. Lets write our very first code on the python shell.
```python
>>> 2 + 3
5
```
In order for you to exit the interactive shell write **exit()** command and press Enter.
```python
exit()
```
>Now, we know how to open and exit the interactive shell. Python will give you results if you write scripts that python understands, if not it returns errors.

Let's practice more how to use python interactive shell. Go to your terminal or command prompt(cmd) and write the word **python**.

The python interactive shell is opened. Let's do some basic mathematic operations (addtion, subtraction, multiplication, division, modulus, expponential). Lets do some
maths first before we write any python code:

* 1 + 1 = 2
* 5 - 2 = 3
* 2 * 4 = 8 
* 5 / 2  = 2.5
* 3 ** 2 = 9

In python we have the following additional operations:

* 5 % 3 = 2-> means finding the remainder
* 3 // 2 = 1 -> means removing the remainder

Open the python interactive shell and lets write a comment at the very beginning of the shell. A *comment* is a part of the code that the python won't execute. 
We can leave a reminder or text in our code to make our code more readable. Python won't run the comment part. In order for us to comment in python it should 
start with a hash (#) symbol. Example of a comment: 
```
# This is a comment
# Be sure to start with a hash
```

Sample code:

```python 
>>> 1 + 1 # addition(+)
2
>>> 5 - 2 # subtractio(-)
3
>>> 2 * 4 # multiplication(*)
8
>>> 5 / 2 # division(/)
2.5
>>> 5 % 3 # Modulus(%) - finding the remainder
2
>>> 3 % 5 # Modulus(%) - finding the remainder
3
>>> 3 // 2 # Floor division operator(//) - it removes the remainder
1
>>> 3 ** 2 # Exponential Operator(**) 0 equivalent to 3^2 or 3 * 3
```

Now we learned how the python interactive shell works. Lets close the opened shell by writing *exit()* on the shell and open it again, lets practice how to write text
on python shell.

```python
>>> 'Hello World' # write hello world string
'Hello World'
>>> "Hello World" # hello world with double quote
'Hello World'
>>> 'This is a text that we wrote'
'This is a text that we wrote'
>>> # We can also use a triple quotes if its more than one line('''''')
>>> '''This is the use of triple quote if the text is more than one line'''
'This is the use of triple quote if the text is more than one line'
>>> # Lets continue using a text editor / code editor
>>> exit()
```
Now lets proceed to the development environment. Download the VScode or your ideal code editor it can be IDE or just a normal text editor
you can even code on a notepad if you want. Anyways lets start coding.

## Basic Python

### Python Syntax
A Python script can be written in python interactive shell or in the code editor. A python file has an extension of .py.

### Python Indentation
Indentation refers to the spaces at the beginning of a code line. Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important. Python uses indentation to indicate a block of code.

### Comments
Comments can be used as a reminder, and a notes for you to easily understand your code. Python won't be running a comment, thus making
your code more neat and more readable.

#### Example of a comments:
```python
    # First comment
    # Second comment
    # Third comment
```
#### Multiline Comment
Multiline comment uses a triple quotes
```python
"""This is a multiline comment
it does take a lot of line 
hello world
""" 
```

#### Data types
Of course, python also have several types of data types. 

#### Number

    * Integer (Int): Positives,Negatives and Zeros. Examples: -2, -1, 0, 1, 2 ...
    * Float: Decimal Numbers. Examples: -2.1, -1.1, 0.0, 1.1, 2.1 ...
    * Complex Numbers: Combination of numbers and some characters. Examples: 1 + j, 4 + 2k ...

#### String 
Collection of more characters that uses a single or double quotes. You can use triple quotes for more than one sentence.

**Examples:**
```python
'Carl'
"Justin"
"""Carl Justin Gamos"""
```

#### Booleans
Data type that uses True or False(Always Uppercase).

**Examples:**
```python
    True # when the value is true
    False # when the value is false
```

#### List
It is a collection of an array similar to JavaScript, C++, and Java.

**Examples:**
```python
[0, 1, 2, 3, 4, 5] # a list of numbers
['Sta Ana', 'Porac', 'Bacolor', 'Floridablanca'] # a list of strings
['Carl', 30, True, 9.81] # a list of different data types
```
#### Dictionary
A python dictionary object is an unordered collection of data.

**Examples:**
```python
{'name': 'Kepler', 'country':'Philippines', age:250, 'is_married':True}
```
#### Tuple
Is an ordered collection of data types like list but cannot be modified. They are immutable.
**Examples:**
```python
('Carl', 'Justin', 'Cinco', 'Gamos')
```
#### Set
Is a collection of data types similar to list and tuple. set is not an ordered collection of items, it stores only unique items.

We will go in detail about each and every python data type.

**Examples:**
```python
{3.14, 9.81, 2.7} # order is not important in set
```
### Checking Data types