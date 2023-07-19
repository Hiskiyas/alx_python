import random
number = random.randint(-10000, 10000)
last_dig = number%10
if number < 0:
    last_dig = (10-last_dig)*-1
    if last_dig > 5:
        print("Last digit of " + str(number)+ " is " +str(last_dig) + " and is greater than 5",end="\n")
    elif last_dig == 0:
        print("Last digit of " + str(number)+ " is " +str(last_dig) + " and is 0",end="\n")
    elif last_dig < 6 and last_dig != 0:
        print("Last digit of " + str(number)+ " is " +str(last_dig) + " and is less than 6 and not 0",end="\n")