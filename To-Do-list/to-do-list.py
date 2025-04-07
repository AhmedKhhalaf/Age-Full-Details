toDoList = []
actions = input("What Do You Need?\n\
1- Add Mission => add OR a\n\
2- Show All List => show\n\
3- Deleat To Do => Add deleat OR d\n\
4- Update Mission => update OR u\n\
5- Exit => exit OR e\n").lower()


while actions != "exit" and actions != "e":
 
    if actions == "add" or actions == "a":
        addToDo = input("What Is the Misiion Do You Need To Add: ").capitalize().strip()
        toDoList.append(addToDo)
        print(f"Mission {addToDo} Been Add To The List")
    elif actions == "show" or actions == "s":
        for mission in toDoList:
            print(f"- {mission}")
            
    elif actions == "deleat" or actions == "d":
        mission_Name_deleat = input("What Mission Need To Deleat: ")
        if mission_Name_deleat in toDoList:
            toDoList.remove(mission_Name_deleat)
            print(f"Mission {mission_Name_deleat} Been Deleated From The List")
        else:
            print("Misson Is Not In The Lsit")

    elif actions == "update" or actions == "u":
        mission_name_update = input("What Mission Need To Update: ").strip()
        new_name_update = input("What Is The New Mission: ").strip()

        if mission_name_update in toDoList:
            toDoList[toDoList.index(mission_name_update)] = new_name_update
            print(f"Mission {new_name_update} Been Updated To The List")
        else:
            print("Mission Is Not In The List")
    elif actions == "e" or actions == "exit":
        break
    
    actions = input("What Do You Need?\n\
1- Add Mission => add OR a\n\
2- Show All List => show\n\
3- Deleat To Do => Add deleat OR d\n\
4- Update Mission => update OR u\n\
5- Exit => exit OR e\n").lower()

    



