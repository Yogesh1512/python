def add(a,b):
    ans=a+b
    print(ans)

def sub(a,b):
    ans=a-b
    print(ans)

def mul(a,b):
    ans=a*b
    print(ans)

def div(a,b):
    ans=a/b
    print(ans)

def fab(n):
    result=[]
    a,b=0,1
    while b<n:
        result.append(b)
        a,b=b,a+b
    print(result)

def fact(a):
    ans=1
    for i in range(1,a+1):
        ans=ans*i

    print(ans)


def prime(n):
    m = 0
    for i in range(2,n):
        if(n%i==0):
            m = 1
            break
    if m:
        print(n,"is not prime")
    else:
        print(n,"is prime")

def prime_fact(a):
    list=[]
    for i in range(1,a):
        if(a%i==0):
            list.append(i)

    print(list)