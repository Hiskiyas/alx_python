import random
number = random.randint(-100, 100)
if number > 0:
    print(str(number) + " is positive",end="\n")
if number == 0:
    print(str(number) + " is zero",end="\n")
if number < 0:
    print(str(number) + " is negative",end="\n")