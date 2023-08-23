#Inheritance - A child class can inherit properties and function of the parent class 
class ParentClass:

    def __init__(self):
        print("Parent class instance")

    def parent_method(self):
        print("Parent class money")

class ChildClass(ParentClass):
    pass

c = ChildClass()
c.parent_method()
       
# p = ParentClass()
# p.parent_method()