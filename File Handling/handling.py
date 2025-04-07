# take diccison from user if need to creat file or already had
creatFile = input("Do You Need To Creat New File Or Not? ").strip().lower()
# Check if need to creat file or not
if creatFile == "yes" or creatFile == "y":
    fileName = input("Enter Your New File Name: ")
    u_file = open(fileName , "x")
    u_file.close()
elif creatFile == "no" or creatFile ==  "n":
    fileName = input("Enter Your File Name: ")
# if user write any thing else (y)(n)
else:
    print("Make Sure You Use (y) or (n)")
# take action from user to know what he need
action = input("What Do You Need?\n1- Read\n2-Write\n3- Add\n4-Exit\n").strip().lower()
# loop to repeat the all quations to user chosse exit 
while action != "e" and action != "exit":
    # action to read file and print the file
    if action in ["r" , "read"]:
        openFile = open(fileName , "r")
        print(openFile.read())
    # Action Write in The file From Begaining
    elif action in ["w" , "write"]:
        openFile = open(fileName , "w")
        newText = input("Enter The Text: ")
        print("Text Is Added")
        openFile.write(newText + "\n")
    # Action Make New Text In End Of File Text
    elif action in ["a" , "add"]:
        openFile = open(fileName , "a")
        newText = input("Enter The Text: \n")
        openFile.write(newText + "\n")
        # Ask If User Need To Add More Text In file or not
        continues = input("Do You Need TO Continue?(y) or (n)").strip().lower()
        while continues != "n" and continues != "no":
            newText = input("Enter The Text: ")
            openFile.write(newText + "\n")
            continues = input("Do You Need TO Continue?(y) or (n)").strip().lower()

    action = input("What Do You Need?\n1- Read\n2-Write\n3- Add\n4-Exit\n").strip().lower()    
else:
    print("Thank You To Use Our App")

openFile.close()


