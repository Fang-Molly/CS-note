'''
Python For Everybody: Exploring Data in Python 3 (by Charles R. Severance)

Exercise 8.4: Download a copy of the file www.py4e.com/code3/romeo.txt. Write a program to open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split function. For each word, check to see if the word is already in a list. If the word is not in the list, add it to the list. When the program completes, sort and print the resulting words in alphabetical order.

Enter file: romeo.txt
['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window','with', 'yonder']
'''


fhand = open('romeo.txt')
list = []

for line in fhand:
    words = line.split()
    for word in words:
        if word in list: continue
        list.append(word)

print(sorted(list))
