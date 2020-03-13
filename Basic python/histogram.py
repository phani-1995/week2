def histogram(lst):
    for i in lst:
        output=''
        k=i
        while (k>0):
            output += '*'
            k=k-1
        print(output)
lst=[4,6,2,10.,16,20]
histogram(lst)