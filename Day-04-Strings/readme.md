<h1 align="center">🐍 30 Days Of Python: Day 4 - Strings</h1>

<img src="https://github.com/cjgamos/30-Days-of-Python/blob/main/img/729px-Python_logo_and_wordmark.svg.png">

# 📘 Day 4

## Strings
Text is a string data type. Any data type written as text is a string. Any data under single or double quote are strings. There are different string methods and built-in functions to deal with string data types. To check the length of a string use the len() method.

## Creating a String
```python
letter = 'P'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be  a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying the python Challenge"
print(sentence)
```
Multiline string is created by using triple single (''') or double quotes ("""). See the example below.
```python
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created this.'''
print(multiline_string)
# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created this."""
print(multiline_string)
```
## String Concatenation

We can connect strings together. Merging or connecting strings is called concatenation. See the example below:

```python
first_name = 'Carl'
last_name = 'Gamos'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) # Carl Gamos
# Checking length of a string using len() built-in function
print(len(first_name))  # 8
print(len(last_name))   # 7
print(len(first_name) > len(last_name)) # True
print(len(full_name)) # 16
```
## Escape Sequences in Strings
In python and other programming languages \ followed by a character. Let's see the most common escape characters:

* \n: new line
* \t: Tab means(8 spaces)
* \\\\\: Back slash
* \\': Single quote (')
* \\": Double quote (")

```python
print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"')

# output
I hope every one is enjoying the Python Challenge.
Are you ?
Days	Topics	Exercises
Day 1	5	    5
Day 2	6	    20
Day 3	5	    23
Day 4	1	    35
This is a backslash  symbol (\)
In every programming language it starts with "Hello, World!"
```
## String Formatting
### Old Style String Formating (% Operator)
In python there are many ways of formating strings. In this section we will cover some of them. The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s", "%d", "%f", "%.f".
* %s - String (or any object with a string representation, like numbers)
* %d - Integers
* %f - Floating point numbers
* %.f - Floating point numbers with fixed precision
```python
# Strings only
first_name = 'Carl'
last_name = 'Gamos'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area) # 2 refers the 2 significant digits after the point

python_libraries = ['Django', 'Flask', 'Numpy', 'Pandas']
formated_string = 'The following are python libraries:%s' % (python_libraries)
print(formated_string) # "The following are python libraries:['Django', 'Flask', 'Numpy', 'Pandas']"
```

**New Style String Formating (str.format)**

This formating is introduced in python version 3.
```python
first_name = 'Carl'
last_name = 'Gamos'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)
a = 4
b = 3
```