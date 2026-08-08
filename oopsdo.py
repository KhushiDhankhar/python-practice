# class is a blueprint for creating objects (real world objects)

#creating class

class Student:
    name="Khushi"
    age=20
    idols=["akshay kumar","kim taehyung"]
    college_name="ABC university"  #class attr

    #   obj attr>class attr

    #parameterized constructor
    def __init__(self,name,marks):  # it is invoked everytime when a object is created
        print("adding new object....")
        self.name=name #self is a reference to this object (u can write other name also at palce of self)
        self.marks=marks #instance attribute (with self)

    def hello(self):  #methods
        print(f"hello {self.name}, welcome to {self.college_name}")

    def getmarks(self):   #object level method
        return self.name,self.marks
    
    def remarks(self):
        if (self.marks>=80):
            print(f"{self.name} is a brilliant student\ncongratulations !!")
        else:
            print(f"{self.name} needs improvement")

    @staticmethod    #decorator
    def welcome():  # without self (class level method)
        print("welcome to OOPS world of python")




s1=Student("khushi",100) #object
s4=Student("abc",23)
# print(s4.name,s4.idols)
# print(s1.name,s1.marks)
# print(s1.age)
# print(s1.idols)
# s3=Student("junkook",100)
# print(s3.age)
s2=Student("kim taehyung",100)
#print(s1,s2)
print(s2.name,s2.marks)

s2.hello()
print(s2.getmarks())
s2.remarks()
s2.welcome()
 
#to delete object or object attribute
del s4.name 
del s4