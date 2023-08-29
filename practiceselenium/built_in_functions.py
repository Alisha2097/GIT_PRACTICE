demo_tuple =(5,7,8,4,5,6,1)
#input()
x=input("Enter your name:")
print("welcome "+x)

#sum()
x = sum(demo_tuple,5)
print(x)

#sorted()
x = sorted(demo_tuple)
print(x)


#slice()
x = slice(2,5,2)
print(demo_tuple [x])

#min()
x = min(demo_tuple)
print(x)

#max()
x = max(demo_tuple)
print(x)

#iter()
i=iter(demo_tuple)
j= reversed(demo_tuple)
print(next(i))
print(next(j))
print(next(i))
print(next(j))