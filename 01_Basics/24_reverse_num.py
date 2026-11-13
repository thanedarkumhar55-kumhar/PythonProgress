num=int(input("Enter any number: "))
reverse=0
if(num<0):
    num=num*(-1)
    while(num!=0):
        digit=num%10
        reverse=(reverse*10)+digit
        num=num//10
    print(f"The reversed value is {-reverse}")
else:
    while(num!=0):
        digit=num%10
        reverse=(reverse*10)+digit
        num=num//10
    print(f"The reversed value is {reverse}")