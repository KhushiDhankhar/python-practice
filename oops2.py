class Car:  #(parent class)

    colour="white"
    
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")

    
class ToyotaCar(Car):  #inheritance (child class)
    def __init__(self,name,type):
        super().__init__(type)
        self.name=name
        super().start()

class Fortuner(ToyotaCar): # due to this multiple inheritance is implemented
    def __init__(self, type):
        self.type=type
        
car1=ToyotaCar("fortuner","electric")
#car2=ToyotaCar("prius","petrol")
car3=Fortuner("petrol")

#car1.start()
print(car1.type)
#car2.start()
# car1.stop()
# car2.stop()
# print(car1.colour)
# print(car3.type)
# car3.start()


#multiple inheritance
class A:
    varA="welcome to class A"

class B:
    varB="welcome to class B"

class C(A,B):
    varC="welcome to class C"

# c1=C()
# print(c1.varC)
# print(c1.varA)
# print(c1.varB)
