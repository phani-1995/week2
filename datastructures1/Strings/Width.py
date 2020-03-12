import textwrap
def wid_display(string):
    print(textwrap.fill(string,width=50))
string=("Checking string width:")
print("Normal string: ",string)
wid_display(string)

