import random
length = int(input("Enter You Pass Length: "))
print("Your Password Is: " , end="")
chars = "1234567890qwertyuioplkjhgfdsazxcvbnm!@#$%QWERTYUIOPLKJHGFDSAZXCVBNM"
for i in range(length):
    print(random.choice(chars) , end="")
