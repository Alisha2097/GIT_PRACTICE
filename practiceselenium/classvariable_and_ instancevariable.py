#class variable = it is not tied to a particular object it is accessible to all 
#instance variable =  a varible that is tied to particular object that you create within the particular class 

class RateofInterest:

    interest =0.06 #class variables  (are accessible to all the instances and objects)
    def __init__(self, name, loan ):
        self.name = name
        self.loan = loan #These are instance variable sepecific to objects (Define the instance variable in init method)
        # self.interest = interest 

    def calculate_interest(self):
        # print("Total interest: ", self.loan *self.interest) self refers to a particular instance 
        print("Total interest: ", self.loan *RateofInterest.interest)

#person1 and person2 is the object that we have created the instances
person1 =RateofInterest("Manish",500000) 
person1.interest = 0.08
person1.calculate_interest()

person2 =RateofInterest("Rahul",400000)
person2.interest = 0.04
person2.calculate_interest()

#Inheritance Example

class RateofInterest:

    interest =0.06 #class variables  (are accessible to all the instances and objects)
    def __init__(self, name, loan ):
        self.name = name
        self.loan = loan #These are instance variable sepecific to objects (Define the instance variable in init method)
        # self.interest = interest 

    def calculate_interest(self):
        # print("Total interest: ", self.loan *self.interest) self refers to a particular instance 
        print("Total interest: ", self.loan *self.interest)

class Student(RateofInterest):
    interest = 0.04

s =Student("Rita",500000)
s.calculate_interest()