th=input("Enter any number or character : ")
if(th.isnumeric()):
    print(f"This is a number. ")
elif(th.isalpha()):
    print(f"This is a character. ")
else: 
    print(f"This is a special charactor.")