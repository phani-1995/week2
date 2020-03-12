def repeat(listOfTuples):
    flag=False

    list1=[]
    cnt=0
    for i in listOfTuples:
        if i in list1:
            flag=True
            continue
        else:
            cnt=0
            for j in listOfTuples:
                if j[0] == i[0] and j[1] == i[1]:
                    cnt=cnt+1

            if (cnt > 1):
                print(i,"-",cnt)
                list1.append(i)
    if flag == False:
        print("No Duplicates")

listOfTuples=[('a','e'),('b','x'),('b','x'),('a','e'),('b','x')]
repeat(listOfTuples)