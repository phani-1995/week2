f_name=input("Enter the first name: ")
l_name=input("Enter the last name: ")
try:
    f1=f_name[: :-1]
    l1=l_name[: :-1]
    print("The first name in reverse is: ",f1)
    print("The last name in reverse is: ",l1)
except:
    print("Enter the correct name")