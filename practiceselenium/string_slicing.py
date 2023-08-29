#s[i:j] - slice of s from i to j 
#s[i:j:k] - slice of s from i to j with step k 
#s[startindex:endindex:step]

s ="welcomeee to software testing mentor and rcv academy"
y='name, age, city'

print(s[0])
print(s[-1])

#slicing from the first
print(s[0:8])

#slicing from the middle with step
print(s[4:8:2])

#By default goes to the end ( if you want whole string )
print(s[:])
print(s[0:]) #both are same

print(s[0:-1])

#to get last part of the string 
print(s[44:])
print(s[-7:])
print(s[-7:-2])

#to reverse string 
print(s[::-1])

print(y.index(','))
print(y[0:y.index(',')])

print(y[y.index(','):8])