def c_rep(list1):
    count=0
    for word in list1:
        val=len(word)-1
        if (word[0]==word[val]):
            count=count+1
    print("words having first and last same is: ",count)
list1=["abc","xyz","aba","1221"]
c_rep(list1)