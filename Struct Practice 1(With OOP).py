# python don't have concept of user defined datatype but this xconcept can be implemended in python using OOP

class Student:
    def __init__(self,name,regnum,marks,percent):
        self.name = name
        self.regnum = regnum
        self.marks = marks
        self.percent = percent

std2 = Student("Zain","23-cs-115",90,90.5)
print(f"Name: {std2.name}")
print(f"Registeration Number: {std2.regnum}")
print(f"Marks: {std2.marks}")
print(f"Percentage: {std2.percent}")

