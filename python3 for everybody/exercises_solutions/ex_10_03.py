'''
Python For Everybody: Exploring Data in Python 3 (by Charles R. Severance)

Exercise 10.3: Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should convert all the input to lower case and only count the letters a-z. Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.
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
