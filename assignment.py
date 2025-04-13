class Person:
    def __init__(self, age, gender):
        self.age = age
        self.gender = gender

class Teacher(Person):
    def __init__(self, age, gender, class_name):
        super().__init__(age, gender)  
        self.class_name = class_name
    
    def teaches(self):
        print("Class name : ", self.class_name)
        print("Age : ", self.age)
        print("Gender : ", self.gender)
        print("I'm a Teacher.")

class Student(Person):
    def __init__(self, age, gender, division):  
        super().__init__(age, gender)
        self.division = division
    
    def studies(self):
        print("Division : ", self.division)
        print("Age : ", self.age)
        print("Gender : ", self.gender)
        print("I study.")

teach = Teacher(20, "F", "FE")
teach.teaches()
print("\n")
stud = Student(18, "M", "P")
stud.studies()