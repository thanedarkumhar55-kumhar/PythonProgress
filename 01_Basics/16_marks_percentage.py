sub1=int(input("Enter the first subject marks : "))
sub2=int(input("Enter the second subject marks : "))
sub3=int(input("Enter the third subject marks : "))
sub4=int(input("Enter the fourth subject marks : "))
sub5=int(input("Enter the fifth subject marks : "))
if((sub1<0 or sub1>100) or (sub2<0 or sub2>100) or (sub3<0 or sub3>100) or (sub4<0 or sub4>100) or (sub5<0 or sub5>100)):
    print("Please enter the value marks value.")
else:
    p=((sub1+sub2+sub3+sub4+sub5)/5)
    print(f"You have scored {p:.2f}%")