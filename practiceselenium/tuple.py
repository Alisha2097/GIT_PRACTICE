#tuple are indexed, allow duplicate values and cannot be modified (immutable)

demo_tuple =(1,2,3,4,5)
demo_tuple1 =("Delhi","Delhi","Mumbai","New York","Kathmandu","Pokahra")
demo_tuple2 = (True,False,False,True)
demo_tuple3 = (True, 1, "Butwal", 23.56 )

# print(demo_tuple1[0])
# print(demo_tuple1[1])

# print(demo_tuple1.append("Kolkata"))

# print(demo_tuple1.pop())

# print(len(demo_tuple2))
# print(type(demo_tuple1))

print(demo_tuple1.count("Delhi"))
print(demo_tuple1.index("New York"))

print(demo_tuple1[3])

for x in demo_tuple1:
    print (x)

joined_tuple =demo_tuple1 + demo_tuple2 + demo_tuple3
print(joined_tuple)
print(type(joined_tuple))


print(demo_tuple2[0:3])