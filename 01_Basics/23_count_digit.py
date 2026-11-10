num=int(input("Enter any number : "))
newnum=num
count=0
if(num<0):
    num=num*(-1)
    while(num!=0):
        num=num//10
        count+=1
    print(f"There are {count} digit in {newnum}")
elif(num==0):
    print(f"There area 1 digit in {num}")
else:
    while(num!=0):
        num=num//10
        count+=1
    print(f"There are {count} digit in {newnum}")