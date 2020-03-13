def concat_lst_str(list):
    result=''
    for ele in list:
        result += str(ele)
    return result
list=[10,20,50,45,53,14,3]
print(concat_lst_str(list))