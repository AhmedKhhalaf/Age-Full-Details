import random
gameList = ["rock", "paper" , "scissors"]
user_guess = input("Enter Your Guess: ").lower().strip()
comGuess = random.choice(gameList)

if comGuess == user_guess:
    print(f"You Tie With Computer We Are {user_guess.capitalize()} Together")
elif comGuess == "rock" and user_guess == "paper":
    print(f"Congrats! You Win The Computer Result Is: {comGuess}")

elif comGuess == "rock" and user_guess == "scissors":
    print(f"Sorry But You loessss The Computer Guess Is: {comGuess}")

elif comGuess == "paper" and user_guess == "scissors":
    print(f"Congrats! You Win The Computer Result Is: {comGuess}")
else:
    print("plz Be sure You Choice Rock OR Paper OR Scissors")

