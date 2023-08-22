x="Python Class"
y="RCV Academy "

#traditional approach 
print("Welcome to "+ x +" from " +y)

#format string using percent operator
print("Welcome to %s from %s" %(x,y))
print("Welcome to %s from %s" %("Java Class",y))

#format method to format string 
print("Welcome to {} from {}".format(x,y))

#format with index ( most used and recommmended)
print("Welcome to {1} from {0}".format(x,y))

#keyword argument 
print("welcome to {classname} from {academyname}".format(classname=x, academyname=y))
print("welcome to {classname} from {academyname}".format(classname="Java", academyname=y))