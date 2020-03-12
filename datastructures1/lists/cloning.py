def cloning(lst):
    lst1_copy=[i for i in lst]
    return lst1_copy

lst=[4,8,2,6,8,9,10]
lst1=cloning(lst)
print("The original list is: ",lst)
print("After cloning the list: ",lst1)
cloning(lst)