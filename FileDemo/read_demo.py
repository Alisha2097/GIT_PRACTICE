f =open("F:\selenium_python\GIT_PRACTICE\\FileDemo\\writedemo.txt","r+")
# print(f.read())
# f.close()

print(f.readline())
print(f.readline())
print(f.readline())

f.close()

f =open("F:\selenium_python\GIT_PRACTICE\\FileDemo\\writedemo.txt","a")
f.write("Some content, Some content")
f.close()