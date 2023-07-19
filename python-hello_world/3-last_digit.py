import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_dig = number%10
else:
    last_dig = number%-10
if last_dig > 5:
    print("Last digit of " + str(number)+ " is " +str(last_dig) + " and is greater than 5")
if last_dig == 0:
    print("Last digit of " + str(number)+ " is " +str(last_dig) + " and is 0")
if last_dig < 6 and last_dig != 0:
    print("Last digit of " + str(number)+ " is " +str(last_dig) + " and is less than 6 and not 0")