class Student_Register:
    def __init__(self,name,age,number,blood):
        self.name = name
        self.age = age
        self.number = number
        self.blood = blood 
        
    def show(self):
        print(f"The Student name is {self.name}")
        print(f"The {self.name} Age is {self.age}")
        print(f"The {self.name} number is {self.number}")
        print(f"The {self.name} Blood Group is {self.blood}")
        
obj1 = Student_Register("Sujal",21,123456,"B+")
obj2 = Student_Register("Dhruv",20,623451,"A+")
obj3 = Student_Register("Riddhi",21,623561,"A-")


obj1.show()
print() 
obj2.show()
print() 
obj3.show()
        
        