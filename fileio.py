
#reading file
'''
filename="hello.txt"
f=open(filename,"r")
data=f.read(6)
data2=f.readline()
data3=f.readlines()
print(data)
print(data2)
print(data3)
f.close()

#appending
g=open(filename,"a")
g.write("\nwelcome to this world")
g.close()

#writing file
fname="demo.txt"
h=open(fname,"w")
h.write("hello python world!!")
#h.writelines
h.close()

#r+ start , no truncate 
#w+ last , truncate
#a+ last , no truncate

with open(filename,"r") as f:
    dat=f.read(12)
    print(dat)

def check_word():
    with open(fname,"r") as k:
        data1=k.read()
        if(data1.find("python")!=-1):
            print("found")
        else:
            print("not found")
        # new_data=data1.replace("hello","greetings")
            print("old data:",data1)
        #print("updated data:",new_data)
        #print("index of python:",l)

# with open(fname,"w") as k:
#     k.write(new_data)
'''


'''
fname="demo.txt"
def check_line():
    data1=True
    word="java"
    line_no=1
    with open(fname,"r") as k:
        while(data1):
            data1=k.readline()
            if(word in data1):
                print("found in line no.",line_no)
                return
            line_no+=1

    print("not found")
        
check_line()
'''

count=0
with open ("sample.txt","r")as c:
    d=c.read()
    nums=d.split(",")
    for val in nums:
        if(int(val)%2==0):
            count+=1
    print(count)