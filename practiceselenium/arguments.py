# Positional Arguments 
# Keyword Arguments 
# Required arguments 
# Optional Arguments 

#those values when you are defining the function are known as parameters 
# when you are calling the function and providing the actual numbers or the values with the called function is called areguments 

def sub_demo(x=5,y=4): #x,y are parameters
    return x-y

z=sub_demo(8,4)# 8,4 arguments 
print(z)

z=sub_demo()# 8,4 arguments 
print(z)

print(sub_demo(8,6))
print(sub_demo(6))
print(sub_demo())

print(sub_demo(y=10,x=6))