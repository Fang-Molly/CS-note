'''
Python For Everybody: Exploring Data in Python 3 (by Charles R. Severance)

Exercise 10.1: Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.

After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.

Sample Line: From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

Enter a file name: mbox-short.txt cwen@iupui.edu 5

Enter a file name: mbox.txt zqian@umich.edu 195
'''

import string

fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = 0
counts = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        for letter in word:
            counts[letter] = counts.get(letter, 0) + 1

lst = list()
for letter, count in list(counts.items()):
    lst.append((count, letter))
    lst.sort(reverse=True)
for count, letter in lst:
    print(letter, count)
