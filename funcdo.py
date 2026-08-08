def cal_sum(a=1,b=3):#param
    sum=a+b
    return sum

print(cal_sum(10,20))#args
print(cal_sum())
def avg(a,b,c):
    return ((a+b+c)/3)

print(avg(10,20,30))

print("hello world","khushi","kim taehyung",sep="@")
print("world")

def facto(n):
    fact=1
    for i in range(n,0,-1):
        fact*=i
    return(fact)

print(facto(5))

def length(a):
    c=0
    for i in a:
        c+=1
    return c

print(length([1,4,3,6]))

def traverse(a):
    for i in a:
        print(i,end=" ")
    print()
traverse([1,2,3])

def usd_to_rs(a):
    return(a*83)
print(usd_to_rs(5))

def check(a):
    if(a%2==0):
        return "even"
    else:
        return "odd"
    
print(check(4))