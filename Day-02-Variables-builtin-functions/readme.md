<h1 align="center">🐍 30 Days Of Python</h1>

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

Valid variable names are: 
```
firstname
lastname
age
country
city
first_name
last_name
capital_city
_if # if we want to use reserved word as a variable
year_2019
year2019
current_year_2019
num1
num2
```
Invalid variable names are:
```
first-name
num-1
1num
```
When we assign a certain data type to a variable, it is called variable declaration. For instance in the example below my first name is assigned to a variable first_name. The equal sign is an assignment operator. Assigning means storing data in the variable.

*Example:*

```python
# Variables in Python

first_name = 'Carl'
last_name = 'Gamos'
country = 'Philippines'
city = 'Pampanga'
age = 20
is_married = False
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Carl',
   'lastname':'Gamos',
   'country':'Philippines',
   'city':'Pampanga'
   }
```
Let us use *print()* and *len()* built in functions. Print will take multiple arguments and print out the string that is inside the parenthesis.

**Example:**

```python
print('Hello, World!')
print('Hello',',', 'World','!') # it can take multiple arguments
print(len('Hello, World!')) # it takes only one argument
```
Let's print and also find the length of the variable.

**Example:**
```python
# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)
```
Variables can also be declared in one line.

**Example:**
```python
first_name, last_name, country, age, is_married = 'Carl', 'Gamos', 'Philippines', 20, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
```
Getting user input using the *input()* function. Let's assign the data we got from a user into first_name and age variables. Example:
```python
first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)
```
## Data Types
There are a ton of data types in python. To identify the data type use the *type* built-in function. I suggest to focus on understanding the different data types very well. When it comes to programming, it is all about data type.

## Checking Data types and Casting
* Check Data types: To check the data type of a certain data or variable we use the *type* **Example:**
```python
# Different python data types
# Let's declare variables with various data types

first_name = 'Carl'     # str
last_name = 'Gamos'       # str
country = 'Philippines'         # str
city= 'Pampanga'            # str
age = 20                   # int, it is not my real age, don't worry about it

# Printing out types
print(type('Asabeneh'))     # str
print(type(first_name))     # str
print(type(10))             # int
print(type(3.14))           # float
print(type(1 + 1j))         # complex
print(type(True))           # bool
print(type([1, 2,3,4]))     # list
print(type({'name':'Carl','age':19, 'is_married':False}))    # dict
print(type((1,2)))                                              # tuple
print(type(zip([1,2],[3,4])))                                   # set
```
* Casting: Casting is converting one data type to another data type. We use *int(), float(), str(), and list()*. When we do an arithmetic operations string numbers should be first converted to int or float otherwise it will return an error. If we concatenate a number with string, the number should be converted to a string first.
```python
# int to float

num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int

gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int
num_str = '10.6'
print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6

# str to list
first_name = 'Carl'
print(first_name)
print(first_name)                    # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']
```
## Numbers
Number data types in python:
1. Integers: Integer(negative, zero and positive) numbers Example: ... -3, -2, -1, 0, 1, 2, 3 ...

2. Floating Point Numbers(Decimal numbers) Example: ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...

3. Complex Numbers Example: 1 + j, 2 + 4j, 1 - 1j

💯 You are awesome. You have just completed day 2 challenges and you are two steps ahead on your way to greatness. Now do some exercises for your brain and for your muscle.

## 💻 Exercises - Day 2

### Exercise #1
1. Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
2. Write a python comment saying 'Day 2: 30 Days of python programming'
3. Declare a first name variable and assign a value to it
4. Declare a last name variable and assign a value to it
5. Declare a full name variable and assign a value to it
6. Declare a country variable and assign a value to it
7. Declare a city variable and assign a value to it
8.Declare an age variable and assign a value to it
9.Declare a year variable and assign a value to it
10.Declare a variable is_married and assign a value to it
11.Declare a variable is_true and assign a value to it
12.Declare a variable is_light_on and assign a value to it
13.Declare multiple variable on one line

### Exercise #2
1. Check the data type of all your variables using type() built-in function
2. Using the len() built-in function find the length of your first name
3. Compare the length of your first name and your last name
4. Declare 5 as num_one and 4 as num_two
    I. Add num_one and num_two and assign the value to a variable _total
    II. Subtract num_two from num_one and assign the value to a variable _diff
    III. Multiply num_two and num_one and assign the value to a variable _product
Divide num_one by num_two and assign the value to a variable _division
Use modulus division to find num_two divided by num_one and assign the value to a variable _remainder
Calculate num_one to the power of num_two and assign the value to a variable _exp
Find floor division of num_one by num_two and assign the value to a variable _floor_division
The radius of a circle is 30 meters.
Calculate the area of a circle and assign the value to a variable area_of_circle
Calculate the circumference of a circle and assign the value to a variable circum_of_circle
Take radius as user input and calculate the area.
Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
Run help('keywords') in python shell or in your file to check for the reserved words