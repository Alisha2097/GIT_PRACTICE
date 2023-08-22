#dictionary ar used to store data in key-value pairs.

demo_dict = {}
demo_dict1 = {1:20,2:45,3:50,6:67}
demo_dict2= {"qa":"testurl","uat":"uaturl"}
demo_dict3= {"qa":"34","3":"uaturl"}

# Adding item to dictionary
demo_dict2['prod']="producturl"
demo_dict2[1]=56
print(demo_dict2)

#Remove item from dictionary
demo_dict2.pop(1)
print(demo_dict2)

print(type(demo_dict1))

print(demo_dict1[1])

print(demo_dict2["uat"])