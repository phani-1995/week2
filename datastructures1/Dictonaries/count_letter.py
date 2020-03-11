def c_str(str1):
    dict22={}
    for count in str1:
        keys=dict22.keys()
        if count in keys:
            dict22[count]+=1
        else:
            dict22[count]=1
    print(dict22)
str1=input("Enter the input: ")
c_str(str1)