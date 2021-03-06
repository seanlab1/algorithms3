'''
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
'''

# def add_digits(num):
#     while num > 10: num = sum([int(x) for x in str(num)])
#     return num

from algorithms3.math import add_digits

print(add_digits(38))