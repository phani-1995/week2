def symm(set1,set2):
    s_diff=set1^set2
    symmDif1 = set1.symmetric_difference(set2)
    print(s_diff)
    print(symmDif1)
set1={'a','e','i','o','u',1,2,3,4,5,6,7,8,9,0,'1'}
set2={'i','1','u',4,3,1,'h','b','v','z'}
symm(set1,set2)