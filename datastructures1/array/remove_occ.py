def remove_occ(arr1):
    for i in range(0,len(arr1)-1):
        for j in range(i+1,len(arr1)-1):
            if arr1[j] == arr1[i]:
                arr1.remove(arr1[j])
arr1=[2,3,4,5,6,6,7,8,9,9,10,11]
remove_occ(arr1)
print(arr1)