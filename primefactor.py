
list=[]

def prime_fact(a):
    for i in range(1,a):
        if(a%i==0):
            list.append(i)

    print(list)

a=int(input("enter the number"))
prime_fact(a)