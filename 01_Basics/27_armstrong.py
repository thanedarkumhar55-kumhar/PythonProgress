num=int(input("Enter any positive number : "))
newnum=num
count=0
sum=0
if(num<=0):
    print(f"Please enter only positive number.")
else: 
    while(num!=0):
        num=num//10
        count+=1
num=newnum
while(num!=0):
        digit=num%10
        num=num//10
        sum=sum+pow(digit, count)
if(newnum==sum):
    print("This is an armstrome number.")
else: 
    print("This is not an armstrome number.")