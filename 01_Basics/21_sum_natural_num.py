num=int(input("Enter the n term of natural number : "))
sum=0
for i in range(1, num+1, 1):
    sum=sum+i
print(f"The sum of fisrt {num} natural number is = {sum}")