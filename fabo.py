a=int(input("Enter a number"))

def fab(n):
    result=[]
    a,b=0,1
    while b<n:
        result.append(b)
        a,b=b,a+b
    print(result)



fab(a)