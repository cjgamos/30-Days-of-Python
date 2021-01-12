<h1 align="center">30 Days of Python</h1>

[<< Day 1](https://github.com/cjgamos/30-Days-of-Python)

<p align="center">
    <img src="https://github.com/cjgamos/30-Days-of-Python/blob/main/img/729px-Python_logo_and_wordmark.svg.png">
</p>

# 📘 Day 2

## Built in functions
Python has a ton of built-in functions that are globally available for you to use. Some of the commonly used functions that are built within it are: *print(), len(), type(), int(), float(), str(), input(), list(), dict(), min(), max(), sum(), sorted(), open(), file(), help(), and dir()*. For more reference go to [python documentation](https://docs.python.org/2/library/functions.html).

<p align="left">
    <img width="600" src="https://github.com/cjgamos/30-Days-of-Python/blob/main/img/builtin-functions.png">
</p>

Let's begin by opening the python interactive shell and start using some commonly used built-in functions.

```python
>>> print("Hello World!") # Prints the text Hello Word!
Hello World!
>>> len("Hello World!") # counts the number of characters in a string including the space
12
>>> type("Hello World!") # checks the data type
<class 'str'>
>>> str(10) # converts the number to string
'10'
>>> int('10') # converts the string to number
10
>>> float(10) # converts the integer to decimal
10.0
>>> input("Enter Name: ") # user inputs
Enter Name: Carl
'Carl'
>>> exit()
```
More built-in functions.
```python
>>> help('keywords') # prints all reserved words

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not

>>> dir(str) # information about the function
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', 
'__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', 
'__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
'__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', 
'__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', 
'__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 
'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 
'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal',
 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 
 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 
 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 
 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 
 'translate', 'upper', 'zfill']
>>>
```
Python has a ton of reserved words. Be sure not to use them and don't declare variables nor functions using those reserved words. We will cover more about the variables later on.

Now that we got ourselves familiarized with some built-in functions. Let's do one more practice before we can move on the next section.

```python
>>> min(20, 30, 40, 50) # gives the minimum value
20
>>> max(20, 30, 40, 50) # gives the maximum value
50
>>> min([20, 30, 40, 50]) # takes the list as an argument and return the min
20
>>> max([20, 30, 40, 50]) # takes the list as an arguement and return the max
50
>>> sum([20, 30, 40, 50]) # takes the list as an arguement and return the sum
140
>>>
```
## Variables
Variables are the case of the computer memory that stores data. Mnemonic variables are recommended to use in many programming languages. A variable refers to a memory address in which the data is stored. Numbers at the begining, special characters, hyphen are not allowed when naming the variables, but they can have a short name (like a,b,c), though it is highly recommended to use a descriptive names (like firstname, lastname, age). Variable Naming Rules in Python: 

    * A variable name must start with a letter or the underscore character
    * A variable name cannot start with a number
    * A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    * Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME are different variables)