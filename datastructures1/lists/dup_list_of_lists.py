import itertools
num=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
print("Original list: ",num)
num.sort()
new_num=list(num for num,_ in itertools.groupby(num))
print("NewList: ", new_num)