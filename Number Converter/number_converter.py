user_numbers = input("Enter Your Number: ").strip()
user_action = input("What Do You Need Binary Or Dicimal:").lower().strip()
def check_action(user_numbers , user_action):
    if user_action == "binary" or user_action == "b" :
        print(bin(int(user_numbers)))

        user_continue = input("DO You Need To Add Another Number (y) OR (n): ").lower().strip()

        if user_continue == "y":
            user_numbers = input("Enter Your Number: ").strip()
            user_action = input("What Do You Need Binary Or Dicimal:").lower().strip()
            check_action(user_numbers ,user_action )
        elif user_continue == "n":
            pass

        else:
            print("Please Check You Enter (y) OR (n)")

    elif user_action == "dicimal" or user_action == "d" :
        print(int(float(user_numbers)))
        user_continue = input("DO You Need To Add Another Number (y) OR (n): ").lower().strip()
        if user_continue == "y":
            user_numbers = input("Enter Your Number: ").strip()
            user_action = input("What Do You Need Binary Or Dicimal:").lower().strip()
            check_action(user_numbers ,user_action )
        elif user_continue == "n":
            pass
        else:
            print("Please Check You Enter (y) OR (n)")

check_action(user_numbers , user_action)