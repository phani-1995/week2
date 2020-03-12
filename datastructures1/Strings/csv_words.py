class sortedcharacters:
    def sortCharatres(self,str):
        strings=sorted(str.split(" "))
        print("".join(str))
    def sortIter(self,Str1):
        Str1=Str1.split(" ")
        leng=len(Str1)-1
        for i in range(leng):
            for j in range(leng-i):
                if(Str1[j]>Str1[j+1]):
                    Str1[j],Str1[j+1]==Str1[j+1],Str1[j]
            print("".join(Str1[j]),end=" ")


Str1="red, white, black, red, green, black,"
sortedwords=sortedcharacters()
sortedwords.sortCharatres(Str1)
sortedwords.sortIter(Str1)