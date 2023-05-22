

def amst(n):
    z=0
    while n>0:
        b=int(n%10)
        n=int(n/10)
        sum=b*b*b
        z=z+sum

    if a==z:
        print("number is amstrong")
    else:
        print("number is not amstromg")




a=int(input("Enter a number"))
amst(a)
