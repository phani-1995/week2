a=[]
n=int(input("Enter a number of elements in a list: "))
for i in range(0,n):
    ele=input("Enter element"+str(i+1)+":")
    a.append(ele)
x=len(a[0])
temp=a[0]
for j in a:
    if (len(j)>x):
        x=len(i)
        temp=i
print("The word with longest length is: ")
print(temp)