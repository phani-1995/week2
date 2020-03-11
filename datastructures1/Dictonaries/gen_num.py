def gen_num(n):
    d=dict()
    for x in range(1,n+1):
        d[x]=x*x
    print(d)
n=int(input("Enter the number of values you want: "))
gen_num(n)