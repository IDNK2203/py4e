# 9.4 Write a program to read through the
# mbox-short.txt and figure out who has
# sent the greatest number of mail messages.
# The program looks for 'From ' lines and
# takes the second word of those lines as
# the person who sent the mail. The program
# creates a Python dictionary that maps the
# sender's mail address to a count of the
# number of times they appear in the file.
# After the dictionary is produced, the
# program reads through the dictionary using
# a maximum loop to find the most prolific committer.


import os

fname = input("Enter file name: ")
email_histo = dict()

dir_path = os.path.dirname(os.path.realpath(__file__))
fpath = os.path.join(dir_path, fname) + '.txt'

with open(fpath, "r") as f:
    for line in f:
        if line.startswith("From "):
            words = line.split()
            email_ = words[1]
            email_histo[email_] = email_histo.get(email_, 0) + 1

max_email = None
max_email_count = None

for k, v in email_histo.items():
    if max_email is None or max_email_count < v:
        max_email = k
        max_email_count = v

print(max_email, max_email_count)
