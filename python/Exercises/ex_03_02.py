"""
Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:

Enter Hours: 20  
Enter Rate: nine  
Error, please enter numeric input  

Enter Hours: forty  
Error, please enter numeric input
"""

hour = input('Enter Hours: ')

try:
    hour = float(hour)
    rate = input('Enter Rate: ')
    rate = float(rate)
except:
    print('Error, please enter numeric input')
    quit()

if hour <= 40:
    pay = hour * rate
else:
    pay = 40 * rate + (hour - 40) * (rate * 1.5)
    
print('Pay:',pay)
