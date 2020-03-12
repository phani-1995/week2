def small(num):
    list2=[]
    for i in range(1,num+1):
        ele=int(input("Enter the elements: "))
        list2.append(ele)
    print("The smallest element is: ",min(list2))
num=int(input("Enter the number of elements in a list: "))
small(num)