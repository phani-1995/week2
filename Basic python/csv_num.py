def csv_num(num):
    lst=[]
    for i in range(num):
        lst.append(i)
    print(lst)
    print(tuple(lst))
num = int(input("Enter the number: "))
csv_num(num)
