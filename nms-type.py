import os
command=input("Enter a command: ")
os.system(command + " > nms.tmp")
os.system("clear")
file=open("nms.tmp","r")
for x in file.readlines():
    file2=open("nms2.tmp","w")
    file2.write(x)
    os.system("cat nms2.tmp | nms -a")
file.close()
os.system("rm nms.tmp")
os.system("rm nms2.tmp")
