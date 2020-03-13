def grp_val(x,y):
    if x in lst1:
        print('True')
    if y in lst1:
        print('True')
    else:
        print('False')
lst1=[1,5,8,3]
x=int(input("Enter the value to search in lst1: "))
y=int(input("Enter the value to be search in lst: "))
grp_val(x,y)