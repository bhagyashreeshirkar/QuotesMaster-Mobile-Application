"""
Write a Python program which accepts a sequence of comma-separated numbers from user
and generate a list and a tuple with those numbers.
Sample data : 3,5,7,23
Output :
List : ['3', '5', '7', '23']
Tuple : ('3', '5', '7', '23')
"""


numbers = input('Enter comma-separated numbers: ')
a = numbers.split(',')
print('List:', a)  # when you split a string it automatically splits into the list
print('Tuple:', tuple(a))
