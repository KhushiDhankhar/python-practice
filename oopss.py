class Circle:
    def __init__(self,radius):
        self.radius=radius

    def Area(self):
        return (22/7)*(self.radius**2)
    
    def Perimeter(self):
        return 2*(22/7)*self.radius
    
c1=Circle(7)
print("area:",c1.Area())
print("perimeter:",c1.Perimeter())

class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary

    def showDetails(self):
        print("role:",self.role)
        print("department:",self.dept)
        print("salary:",self.salary)

class Engineer(Employee):
    def __init__(self, name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer", "IT", 250000)

e1=Employee("consultant","education",100000)
e1.showDetails()
e2=Engineer("khushi",20)
e2.showDetails()

class Order():
    def __init__(self,item,price):
        self.item=item
        self.price=price

    # def __gt__(self,o2):
    #     if (self.price>o2.price):
    #         print(f"order of {self.item} is greater than order of {o2.item}")
    #     else:
    #         print(f"order of {o2.item} is greater than order of {self.item}")
        
    def __gt__(self,o2):
        return self.price>o2.price
o1=Order("pens",20)
o2=Order("notebook",40)
print(o1>o2)