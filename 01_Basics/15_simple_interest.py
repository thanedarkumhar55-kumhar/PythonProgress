p=int(input("Enter the Principal value : "))
r=int(input("Enter the rate in percentage : "))
t=int(input("Enter the time in year : "))
if(p<=0):
    print("please enter the valid principal value.")
elif(r<0):
    print("Please enter the valid rate value.")
elif(t<0):
    print("Please enter the valid time value.")
else: 
    si=((p*r*t)/100)
    total=p+si
    print(f"principal value = {p}")
    print(f"Simple interest = {si}")
    print(f"The total amount you have to pay {total}")