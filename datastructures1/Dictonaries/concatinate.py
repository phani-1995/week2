def merge(dic1,dic2,dic3):
    res={**dic1, **dic2, **dic3}
    return res

dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic4=merge(dic1,dic2,dic3)
merge(dic1,dic2,dic3)
print("The updated dictonary is: ",dic4)
