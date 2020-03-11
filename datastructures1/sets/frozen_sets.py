def frozen(student):
    key=frozenset(student)
    print("The frozen set is: ", key)
student={"name":"ankit","age":20,"sex":"Male","college":"NIT Warangal","Address":"Warangal"}
frozen(student)