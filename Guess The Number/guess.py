import random
u_number = int(input("Enter Your Guess Number: "))
c_number = random.randint(0,100)
while c_number != u_number:
    if u_number > c_number:
        print("You Number Is Greater Than Computer Number")
        u_number = int(input("Enter Your Guess Number: "))
    elif u_number < c_number:
        print("You Number Is Smaller Than Computer Number")
        u_number = int(input("Enter Your Guess Number: "))
else:
    print(f"Your Guessing The True Number: {c_number}")