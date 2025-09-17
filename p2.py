Number = int(input("Enter number NOW~!"))
Kill_Number = int(input("Kill number here:"))

while Number<=Kill_Number:
    if Kill_Number%Number==0:
        print(Number)
        Number += 1
        
