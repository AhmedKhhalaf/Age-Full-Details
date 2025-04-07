userFileName = input("Enter Your File Name: ")
MyOpenFile = open(userFileName , encoding="utf-8")
letterCount = 0
WordsCount = 1
sentenceCount = 0
for row in MyOpenFile:
    for letter in row:
        if letter != " ":
            letterCount+=1
            
        if letter == " ":
            WordsCount+=1

        if letter == "?" or letter == "!" or letter == ".":   
            sentenceCount+=1
MyOpenFile.close()
print(f"The Letters In Your File Is: {letterCount} Letters And You Have {WordsCount} Words And {sentenceCount} Sentance")
