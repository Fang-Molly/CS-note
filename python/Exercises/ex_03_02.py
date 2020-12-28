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
