#scope is the boundary of variable 
#LEGB rule: Local -> Enclosing  -> Global -> Buil

# x=20 #global scope variable

# def var_scope_demo():
#     # x=20 # local scope variable 
#     global x
#     x=20
#     print(x)

# def var_scope_demo1():
#     print(x)
    
# var_scope_demo()
# var_scope_demo1()

#Enclosing

x=100
def var_scope_demo():
    # x=20 # local scope variable 
    # global x
    # x=20
    print(x)
    def var_scope_demo1():
        # x=50
        print(x)
        def grandchild():
            # x=40
            print(x) #enclsoing scope is the parent function
        grandchild()
    var_scope_demo1()
var_scope_demo()