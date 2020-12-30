'''
Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).

Enter Hours: 45
Enter Rate: 10
Pay: 475.0
'''

def computepay(hour, rate):
    if hour <= 40:
        pay = hour * rate
    else:
        pay = 40 * rate + (hour - 40) * (rate * 1.5)
    return pay

hour = input("Enter Hours: ")
hour = float(hour)
rate = input("Enter Rate: ")
rate = float(rate)

pay = computepay(hour, rate)

print("Pay:", pay)
