user_Number = []
user_NumberInt = int(input("How Many Number do You Need: "))
while user_NumberInt >0:
    user_NumberInt-=1
    user_int = int(input("Enter Your Number: "))
    user_Number.append(user_int)

def avg(n):
    return sum(n) / len(n)

print(f"The Avrage For Your Numbers Is: {int(avg(user_Number))} And The Sum OF The Number Is: {sum(user_Number)} And The Big Number Is: {max(user_Number)} \
And Your Min Number Is: {min(user_Number)}")

