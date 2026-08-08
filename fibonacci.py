f=0
s=1
n=int(input("enter no. till u want series:"))
for i in range(0,n):

    t=f+s
    print (f)
    f=s
    s=t

def fib(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return(fib(n-1)+fib(n-2))

print(fib(3))