# Day 2: 30 Days of Python Programming

#Variables in python
firstname = 'Carl'
lastname = 'Gamos'
fullname = 'Carl Justin Gamos'
country = 'Philippines'
city = 'Pampanga'
age = 20
year = 2021
is_married = False
skills = ['Python', 'C++', 'JavaScript', 'Java']
personal_info = {
    'firstname': 'Carl',
    'lastname': 'Gamos',
    'country': 'Philippines',
    'city': 'Pampanga'
}

# Printing the values stored in the variables

print('First Name:', firstname)
print('First Name Length: ', len(firstname))
print('Last Name:', lastname)
print('Last Name Length: ', len(lastname))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Personal Information: ', personal_info)

# Declaring multiple variables in on line

first_name, last_name, country, age, married = 'Carl', 'Gamos', 'Philippines', 20, False

print(first_name, last_name, country, age, is_married)
print('First Name: ', first_name)
print('Last Name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)