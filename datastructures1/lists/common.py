def common_lst(lst1,lst2):
    for i in lst1:
        for j in lst2:
            if (i==j):
                print(i,end="")
lst1=["apple",3,4,7,6,8,"Pine apple",9,10,12]
lst2=["orange",4,6,8,7,"Grapes",13,"apple"]
common_lst(lst1,lst2)