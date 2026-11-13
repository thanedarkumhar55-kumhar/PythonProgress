strng=input("Enter any word. ")
lst=["a", "e", "i", "o", "u"]
th=[]
for i in strng: 
    if(i in lst and i not in th):
        th.append(i)
    else: 
        pass
print(f"The vowel in {strng} are {th}")