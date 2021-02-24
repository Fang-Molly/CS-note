'''
Python For Everybody: Exploring Data in Python 3 (by Charles R. Severance)

Exercise 9.5: This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.

python schoolcount.py Enter a file name: mbox-short.txt {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7, 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
'''


domain_counts = dict()

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
    word = words[1]
    email = word.split('@')
    domain = email[1]
    domain_counts[domain] = domain_counts.get(domain,0) + 1

print(domain_counts)
