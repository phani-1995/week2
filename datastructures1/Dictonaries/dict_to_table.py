# program to print a dictionary in table format.
my_lst={"Name":["Jagadish","Santosh","Haneef"], "Salary":["30K","40K","50K"]}
for row in zip(*([key] + (value) for key, value in sorted(my_lst.items()))):
    print(*row)

