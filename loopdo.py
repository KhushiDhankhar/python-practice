# for i in range(1,11):
#     print(i,end=" ")
# print()

# i=1
# while(i<=10):
#     print(i, end=" ")
#     i+=1
# print()

# for i in range(10,0,-1):
#     print(i, end=" ")
# print()

# a=int(input("enter a number:"))
# for i in range(1,11):
#     print(a,"X",i,"=",a*i)
# print()

# h=[1,4,9,16,25,36,49,64,81,100]
# i=1
# while i<len(h):
#     print(h[i],end=" ")
#     i+=1
# print()
# x=int(input("enter number to search:"))
# h=(1,4,9,16,25,36,49,64,81,100)
# i=1
# while i<len(h):
#     if(x==h[i]):
#         print(" item found at index:",i)
#         break
#     i+=1
# print()
# for i in range(0,len(h)):
#     if(x==h[i]):
#         print(" item found at index:",i)
#         break
    
# print()
sum=0
h=int(input("enter number"))
for i in range(h+1):
    sum+=i
print(sum)

n=int(input("enter number for fact"))
fact=1
for i in range(n,0,-1):
    fact*=i
print(fact)
