hour = input('Enter Hours: ')
hour = float(hour)
rate = input('Enter Rate: ')
rate = float(rate)

if hour <= 40:
    pay = hour * rate
else:
    pay = 40 * rate + (hour - 40) * (rate * 1.5)

print('Pay:',pay)
