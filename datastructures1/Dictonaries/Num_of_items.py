def num_of_items(d):
    # values=sum(map(len,data.values()))
    # print(values)
    count=0
    for x in d:
        if isinstance(d[x],list):
            count += len(d[x])
            print(count)
d = {'A': [1, 2, 3, 4, 5, 6, 7, 8, 9],
     'B': 34,
     'C': 12,
     'D': [7, 8, 9, 6, 4]}
num_of_items(d)