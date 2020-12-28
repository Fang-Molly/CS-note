# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
# Enter Hours: 45  
# Enter Rate: 10  
# Pay: 475.0

hour = input('Enter Hours: ')
hour = float(hour)
rate = input('Enter Rate: ')
rate = float(rate)

if hour <= 40:
    pay = hour * rate
else:
    pay = 40 * rate + (hour - 40) * (rate * 1.5)

print('Pay:',pay)
