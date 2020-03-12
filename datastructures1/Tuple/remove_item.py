def rem_item(tuple2):
    val=list(tuple2)
    val.remove(6)
    print(tuple(val))
tuple2=(1,2,4,6,5,7,8,9,10)
rem_item(tuple2)