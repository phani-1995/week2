def rem1(list3):
    res=[]
    for i in list3:
        if i not in res:
            res.append(i)
    print("The list after removing duplicates is: ", str(res))
list3=[1,2,4,6,8,6,5,2,4,9,10]
rem1(list3)