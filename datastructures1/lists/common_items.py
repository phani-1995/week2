def common_items(a,b):
    a_set=set(a)
    b_set=set(b)
    if (a_set & b_set):
        print(a_set & b_set)
    else:
        print("no common elements")
a=[2,3,4,6,7,9,8]
b=[2,4,1,11,12,13]
common_items(a,b)