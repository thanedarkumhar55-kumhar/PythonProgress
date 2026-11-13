num=int(input("Enter any number : "))
newnum=num
reverse=0
if(num<0):
    newnum=newnum*(-1)
    num=num*(-1)
    while(num!=0):
        digit=num%10
        reverse=(reverse*10)+digit
        num=num//10
else: 
    while(num!=0):
            digit=num%10
            reverse=(reverse*10)+digit
            num=num//10
if(newnum==reverse):
     print(f"This is a palindrome number.")
else: 
     print(f"This is not a palindrome number.")