l=int(input("Enter the length of rectangle : "))
b=int(input("Enter the breadth of rectangel : "))
if(l<=0 and b<=0):
    print("Please enter valid value.")
else:
    area=l*b
    p=2*(l+b)
    print(f"The area of rectangle is {area}")
    print(f"The perimeter of rectangle is {p}")
    