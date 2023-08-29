class Employee:

    # pass #to avoid the error 
    def __init__(self, fname, lname, email):
        self.fname = fname 
        self.lname = lname
        self.email = email 

    def greet_person(self):
        print("Hello ! Welcome " + self.fname)

emp1 = Employee('Seema','Thapa','demo@gmail.com')
emp2 = Employee('Ram','Lama','ram@gmail.com')

print(emp1.fname)
print(emp2.fname)

emp1.greet_person()
emp2.greet_person()