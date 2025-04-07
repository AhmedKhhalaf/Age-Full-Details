u_numberOne = int(input("Enter Your First Number: "))
u_numberTwo = int(input("Enter Your Second Number: "))
operations = input("What is Your Opereation (+) or (x) or (-) or (÷) or (**) or (%): ")

def contanitan(n1 , n2):
    return n1 + n2

def times(n1,n2):
    return n1 * n2

def minass(n1 ,n2):
    return n1 - n2


def divison(n1,n2):
    return int(n1 / n2)

def owss(n1,n2):
    return n1**n2

def divisonplus(n1,n2):
    return n1 % n2

if operations == "+":
    print(contanitan(u_numberOne ,u_numberTwo ))
elif operations == "x":
    print(times(u_numberOne ,u_numberTwo ))
elif operations == "-":
    print(minass(u_numberOne ,u_numberTwo ))
elif operations == "÷":
    print(divison(u_numberOne ,u_numberTwo ))
elif operations == "**":
    print(owss(u_numberOne ,u_numberTwo ))
else:
    print(divisonplus(u_numberOne ,u_numberTwo ))

