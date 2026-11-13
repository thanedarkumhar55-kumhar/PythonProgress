num=int(input("Enter any number : "))
sum=0
if(num<0):
    num=num*(-1)
    while(num!=0):
        digit=num%10
        sum=sum+digit
        num=num//10
else: 
    while(num!=0):
        digit=num%10
        sum=sum+digit
        num=num//10
print(f"This sum of digit is {sum}")