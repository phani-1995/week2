#Difference of two lists using set() method
def diff(lst1,lst2):
    return (list(set(lst1) - set(lst2)))
lst1=[20,25,18,15,30]
lst2=[25,16,17,20]

print(diff(lst1,lst2))
