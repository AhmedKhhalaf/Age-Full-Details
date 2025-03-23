age = int(input("What\'s Your Age: ")) 
mage = age * 12
wage = mage * 4
dage = age * 365
hours = dage * 24
minutes = hours * 60
second = minutes *60
print(f"Your Age is: {age}\nYou live {mage} Month\n{wage:,} Week \n{dage} Day\n{hours:,} Hours\n{minutes:,} Minutes\n{second:,} Second")