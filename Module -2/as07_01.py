# 7.1 Write a program that prompts for a file name,
# then opens that file and reads through the file,
# and print the contents of the file in upper case.
# Use the file words.txt to produce the output below.

# Use words.txt as the file name
# import os


fname = input("Enter file name: ")
fh = open('/home/idnk/SWD/Py4e/Module -2/words.txt')
for line in fh:
    print(line.rstrip().upper())


# dir_path = os.path.dirname(os.path.realpath(__file__))
# with open(os.path.join(dir_path, "words.txt"), "r") as f:
#     for line in f:
#         print(line.rstrip().upper())
