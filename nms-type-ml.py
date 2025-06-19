import os
maxlc=input("Enter the number of lines to show at a time: ")
command=input("Enter a command: ")
os.system(command + " > nms.tmp")
os.system("clear")
file=open("nms.tmp","r")
linecount=0
for x in file.readlines():
    linecount=linecount+1
    if linecount == 1:
        file2=open("nms2.tmp","w")
        file2.write(x)
    elif linecount % maxlc == 0: 
        file2=open("nms2.tmp","w")
        file2.write(x)
        os.system("cat nms2.tmp | nms -a")
    else:
        file2=open("nms2.tmp","a")
        file2.write(x)
file.close()
os.system("rm nms.tmp")
os.system("rm nms2.tmp")
