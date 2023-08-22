# break - break out from loop
#continue - continue in while loop and skip any statement below the continue statement
x = 0
y = 0
while x <= 10:
    print(x)
    x = x + 1
    print("parent while")
    while y < 5:
        print(y)
        y =y+1
        continue
        print("inner loop")
print("out of while loop")

x = 0

while x <= 10:
    print(x)
    x = x + 1
    if x==5:
        break #any statement below else clause gets skipped 
else:
    print("out of while loop")