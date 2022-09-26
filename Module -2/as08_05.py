# 8.5 Open the file mbox-short.txt and read it
# line by line. When you find a line that
# starts with 'From ' like the following line:

# -----------------------------
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# -----------------------------

# You will parse the From line using split() and
# print out the second word in the line (i.e.
# the entire address of the person who sent the
# message). Then print out a count at the end.

# Hint: make sure not to include the lines that
# start with 'From:'. Also look at the last line
# of the sample output to see how to print the count.

# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

import os

fname = input("Enter file name: ")
_low = []
dir_path = os.path.dirname(os.path.realpath(__file__))
fpath = os.path.join(dir_path, fname) + '.txt'

count = 0
with open(fpath, "r") as f:
    for line in f:
        if line.startswith("From "):
            count += 1
            _l = line.rstrip()
            __l = _l.split()
            print(__l[1])
    print("There were", count, "lines in the file with From as the first word")
