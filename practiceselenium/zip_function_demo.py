#zip maps 1 to 1
list1 = ["Nepal","USA","Australia","UK"]
list2= ["Kathmandu","New York","Sydney","London","Melbourne"]

total_cost= [45,65,67,87]
sale_price= [55,77,89,76]

# s = zip(list1,list2)
# print(list(s))

for x,y in zip(total_cost,sale_price):
    print(y-x)