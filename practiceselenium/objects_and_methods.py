#creating the class
class AreaRect:

    def __init__(self,l,b) :  #self will reference to the oject that are being created by using this particular class
        self.l =l
        self.b =b

    #calculate_area method 
    def calculate_area(self):
        return self.l * self.b 
    
area1 = AreaRect(8,5) #area1 holds the object 
area2 = AreaRect(67,76)

print(area1.calculate_area())
print(area2.calculate_area())
        