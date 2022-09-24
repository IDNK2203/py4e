# 8.4 Open the file romeo.txt and read it
# line by line. For each line, split the
# line into a list of words using the split()
# method. The program should build a list of
# words. For each word on each line check to
# see if the word is already in the list and
# if not append it to the list. When the
# program completes, sort and print the
# resulting words in python sort() order as
# shown in the desired output.

# You can download the sample data at http://www.py4e.com/code3/romeo.txt
import os

fname = input("Enter file name: ")
_low = []
dir_path = os.path.dirname(os.path.realpath(__file__))
fpath = os.path.join(dir_path, fname) + '.txt'
with open(fpath, "r") as f:
    for line in f:
        _l = line.rstrip()
        __l = _l.split()
        for x in __l:
            if x in _low:
                continue
            _low.append(x)
    print(sorted(_low))
