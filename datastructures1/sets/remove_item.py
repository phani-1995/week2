def remove_item(set1,set2):
    set1.discard(22)
    set2.discard("abc")
    print(set1)
    print(set2)
set1=set([10,20,22,33,55,20])
set2={"abc","Movie","Education","Games","Exam"}
remove_item(set1,set2)