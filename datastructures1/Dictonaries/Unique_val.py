dict11=[{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"},{"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
print("The original dictonary is: ",dict11)
unique_val=set(val for i in dict11 for val in i.values())
print("Unique values: ",unique_val)