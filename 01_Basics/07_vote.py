age=int(input("Etner your age : "))
if(age<=0):
    print(f"Please enter valid age.")
elif(age<18):
    print(f"You are not eligible for vote.")
else: 
    print(f"You are eligible for vote.")
