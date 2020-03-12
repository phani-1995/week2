class generatePermutation:
    def permutations(self,ele):
        for i in range(len(ele)):
            for j in range(len(ele)):
                for k in range(len(ele)):
                    if (ele[i] != ele[j] != ele[k]):
                        if (ele[i] != ele[k]):
                            print("[",ele[i],ele[j],ele[k],"]")
ele=[1,2,3]
permu=generatePermutation()
permu.permutations(ele)