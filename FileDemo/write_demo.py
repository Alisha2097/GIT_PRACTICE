# f = open("F:\selenium_python\GIT_PRACTICE\\FileDemo\\writedemo.txt","w")
# f.write("This is first line")
# f.close()

f = open("F:\selenium_python\GIT_PRACTICE\\FileDemo\\writedemo1.txt","a")
l = [65, 78, 989, 877, 8787]
for items in l:
    f.write(str(items)+ "\n") #only accepts strings 
f.close()