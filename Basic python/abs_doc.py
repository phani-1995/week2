num=int(input('Enter the number: '))
try:
    num = abs(num)
    print(num)
    print(num.__doc__)
    print(abs.__doc__)
except:
    print("Enter the correct input: ")
