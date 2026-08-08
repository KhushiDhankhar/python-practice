class Person:
    name="anonymous"

    # def changeName(self,name):
    #     #Person.name=name #method1
    #     self.__class__.name=name  #method2 obj ki class
 
    @classmethod
    def changeName(cls,name):   # class->cls
        cls.name=name
# p1=Person()
# p1.changeName("kim taehyung")
# print(p1.name)
# print(Person.name)


#implementing polymorphism
#operator overloading

class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def show_no(self):
        print(self.real,"+",self.img,"i")

    #dunder function are those with double underscore
    def __add__(self,num2):
        newr=self.real+num2.real
        newi=self.img+num2.img
        return Complex(newr,newi)

    def __sub__(self,num2):
        newr=self.real-num2.real
        newi=self.img-num2.img
        return Complex(newr,newi)


num1=Complex(1,3)
num1.show_no()

num2=Complex(4,1)
num2.show_no()

num3=num1+num2
num3.show_no()

num4=num1-num2
num4.show_no()