#len()- "returns the number of items in an object"
x="rcv academy rcv academy rcv academy rcv academy"
y=756473687

# print(y.find("12"))
print(len(x))
# "converts value into a string"
print(str(y)) 

z=str(y)
print(z.find("73"))

#upper() - converts into uppercase
a =x.upper()

#count(sub[, start[, end]])
print(x.count("rcv",18,30))

#isupper() - returns true if all upper
print(a.isupper())
print(a.islower())

#split() splits the string at the specified separator and returns a list

print(x.split())

#rsplit() splits a string list,starting from the right 
#strip() returns a trimmed version of the string 

print(x.rstrip(';7\''))

print(x.replace("rcv","stm",2))

print(x.find("rcv"))

print(x.index("rcv"))