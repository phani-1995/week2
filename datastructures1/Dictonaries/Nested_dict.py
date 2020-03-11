# converting a list into a nested dictionary of keys.
num_lst=[1, 2, 3, 4, 5]
dict12=current={}
for i in num_lst:
    current[i]={}
    current=current[i]
print(dict12)