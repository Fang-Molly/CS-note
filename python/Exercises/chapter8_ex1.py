"""
Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance

Chapter 8: Lists

Exercise 1: 
Write a function called chop that takes a list and modifies it, removing the first 
and last elements, and returns None. Then write a function called middle that takes 
a list and returns a new list that contains all but the first and last elements.  

Solution by Fang, June 28, 2020
"""


def chop(list):
    del list[0]
    del list[-1]

def middle(list):
    new_list = list[1:]
    del new_list[-1]
    return new_list

list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]

print(chop(list1))
print(middle(list2))
