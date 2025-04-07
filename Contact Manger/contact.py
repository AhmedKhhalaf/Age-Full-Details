peopels = {

}
action = input("Add Or Search Or Deleate OR Exit: ").lower().strip()
while action != "exit" and action != "e":
    if action == "add" or action == "a":
        name = input("New Name: ").strip().capitalize()
        n_number = input(f"{name} Number: ")
        peopels[name] = n_number
    
    elif action == "search" or action == "s":
        nameSearch = input("What Is The Name: ").capitalize()
        if nameSearch in peopels:
            print(f"{nameSearch} Number Is: {peopels[nameSearch]}")
        else:
            print(f"{nameSearch} Is Not In The Contact")

    elif action == "deleate" or action == "d":
        nameSearch = input("What Is The Name: ")
        if nameSearch in peopels:
            del peopels[nameSearch]
            print(f"{nameSearch} Is Deleat From Contact")
        else:
            print(f"{nameSearch} Is Not In The Contact")
    action = input("Add Or Search Or Deleate OR Exit: ").lower().strip()
else:
    pass