def difference(A,B):
    res1=A.difference(B)  # Set A - Set B  i.e elements present in A but not in B
    res2=B.difference(A)  #Set B - Set A i.e elements present in B but not in A
    print(res1)
    print(res2)
A={10,20,30,35,40,45}
B={20,30,50,55,40,80}
difference(A,B)