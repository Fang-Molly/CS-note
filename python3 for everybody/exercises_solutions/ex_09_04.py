'''
Python For Everybody: Exploring Data in Python 3 (by Charles R. Severance)

Exercise 9.4: Add code to the above program to figure out who has the most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print how many messages the person has.

Enter a file name: mbox-short.txt cwen@iupui.edu 5

Enter a file name: mbox.txt zqian@umich.edu 195
'''

email_counts = dict()
maximum = 0
max_email = ''

fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    email = words[1]
    email_counts[email] = email_counts.get(email,0) + 1

for email in email_counts:
    if email_counts[email] > maximum:
        maximum = email_counts[email]
        max_email = email

print(max_email, maximum)
