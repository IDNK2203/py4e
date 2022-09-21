# 7.2 Write a program that prompts for a file name,
# then opens that file and reads through the file,
# looking for lines of the form:

# X-DSPAM-Confidence:    0.8475

# Count these lines and extract the floating point
# values from each of the lines and compute the
# average of those values and produce an output as
# shown below. Do not use the sum() function or a
# variable named sum in your solution.
import os

fname = input("Enter file name: ")
c = 0
s = 0

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir_path, fname), "r") as f:
    for line in f:
        if not line.startswith("X-DSPAM-Confidence:"):
            continue
        else:
            c = c+1
            s = s+float(line[line.index(':')+1:].strip())
    avg = s/c
    print('Average spam confidence:', avg)
