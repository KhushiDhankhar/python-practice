class Student:
    
    def __init__(self,name,chem,phy,maths):
        self.name=name
        self.chem=chem
        self.maths=maths
        self.phy=phy

    @property
    def percentage(self):
        return str((self.phy+self.chem+self.maths)/3)+"%"
    #whenever any marks change percentage will also be changed without explicitly running method 
    #due to property method -> attribute

    def avg(self):
        c=(self.chem+self.maths+self.phy)/3
        print(f"name of student {self.name}\nAverage of marks =",c)


s1=Student("khushi",95,89,87)  #u can also take marks as list
# s1.avg()
# s1.name="junkook" #manipulating name
# s1.avg()
print(s1.percentage)
s1.chem=100
print(s1.percentage)

class Account:
    def __init__(self,bal,acc,pswd):
        self.bal=bal
        self.acc=acc
        self.__pswd=pswd  #private method cannot access it (done using two underscore)
          # can access it using function but not directly 
    
    # creating private method
    def __welcome(self):
        print("welcome to incognito mode")

    #accessing private method and attribute
    def reset_pswd(self):
        self.__welcome()
        print("password:",self.__pswd)


    #debit method 
    def debit(self,amount):
        self.bal-=amount
        print(f"debited amount = {amount}")
        self.show()
        
    #credit method
    def credit(self,amount):
        self.bal+=amount
        print(f"credited amount = {amount}")
        self.show()

    #printing balance
    def show(self):
        print("your account no.:",self.acc,"and balance :",self.bal)
        

# a1=Account(10000,"12345","abcd#")
# a1.show()
# a1.credit(90000)
# a1.debit(200)
# a1.reset_pswd()