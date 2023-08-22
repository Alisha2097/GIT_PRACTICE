#dictionary ar used to store data in key-value pairs.

demo_dict = {}
demo_dict1 = {1:20,2:45,3:50,6:67}
demo_dict2= {"qa":"testurl","uat":"uaturl","prepod":"preurl"}
demo_dict3= {"qa":"34","3":"uaturl"}

demo_dict2.update({"prod":"produrl"})

demo_copy=demo_dict2.copy()

print(demo_dict2)
print(demo_copy)

demo_copy.clear()
print(demo_copy)

print(demo_dict2.get("prepod"))

print(demo_dict2.keys())

print(demo_dict2.items())

print(demo_dict2.values())

print(demo_dict2.pop("qa"))

print(demo_dict2.popitem())

print(demo_dict2.popitem())



