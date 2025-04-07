user_number = int(input("Enter Your Total Number: "))
taxRate = int(input("Enter Your Tax Rate: "))
def tax(number , rate):
    return int(number * (rate/ 100))

print(f"Your Tax Is: {tax(user_number , taxRate)} $")
print(f"And Total Number After Tax Is: {user_number + tax(user_number , taxRate)} $")
