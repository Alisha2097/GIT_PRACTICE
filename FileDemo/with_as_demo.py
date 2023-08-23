# fw =open ("demofile.txt","w")
# fw.write("1st Line")
# fw.close()

# fr = open("demofile.txt","r")
# print(fr.read())
# fr.close()

with open("demofile.txt","a") as fw:
    fw.write("This line is from with opertaion")

with open("demofile.txt","r") as fr:
    print(fr.read())

