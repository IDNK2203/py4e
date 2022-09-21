# 5.2 Write a program that repeatedly prompts a user for
# integer numbers until the user enters 'done'. Once
# 'done' is entered, print out the largest and smallest
# of the numbers. If the user enters anything other than
# a valid number catch it with a try/except and put out
# an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.

largest = None
smallest = None
usernum = []

while True:
    try:
        num_ = input("Enter a number: ")
        if num_ == "done":
            break
        num = int(num_)
        usernum.append(num)
    except:
        print("Invalid Input")
for i in usernum:
    if smallest is None:
        smallest = i
    elif smallest > i:
        smallest = i
print("Minimum is", smallest)
for i in usernum:
    if largest is None:
        largest = i
    elif largest < i:
        largest = i
print("Maximum is", largest)


# Steps
# - create an indefinite loop that.
#   - ask the user for an input.
#   - check the user input if it meets the break out criteria.
#   - while the the loop is going on store the users input.
#   - perform a largest and smallest input check. [x]
#   - if the user inputs an input display error message and skip the current iteration.
