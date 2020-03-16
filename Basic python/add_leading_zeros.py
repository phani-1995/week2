#program to add leading zeroes to a string.
test_string="ABC"
#Printing original string
print("The original string: ", str(test_string))
#No of zeros required
N=6
#Using rjust adding leading zero
res=test_string.rjust(N + len(test_string), '0')
print("The string after adding leading zeros: ", str(res))
