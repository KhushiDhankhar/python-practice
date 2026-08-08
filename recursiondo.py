def fact(n):
    if(n==1 or n==0 ):
        return 1
    return n*fact(n-1)

print(fact(3))

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(3)

def fib(a):
    if(a==1 or a==2):
        return 1
    else:
        return fib(a-1)+fib(a-2)
    a=1
    b=1
    c=a+b
print(fib(6))

def cal_sum(a):
    if a==0:
        return 0
    else:
        return a+cal_sum(a-1)

print(cal_sum(0))

def showl(list,idx=0):
    if (idx==len(list)):
        return
    else:
        print(list[idx])
        showl(list,idx+1)
showl(['v','taetae','kim taehyung','taeguaa'],0)