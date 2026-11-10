year=int(input("Enter any year value : "))
if(year%400==0 or (year%4==0 and year%100!=0)):
    print("This is a leap year.")
else:
    print("This is not a leap year.")