import os
print("This script must be run as root or a user with sudo privileges.")
print("This script requires the packages git, gcc and make.")
yay=input("Do you use yay as your package manager? (y/N) ")
if yay.lower()=="y":
    os.system("yay -S no-more-secrets")
else:
    os.system("git clone https://github.com/bartobri/no-more-secrets.git")
    os.system("cd no-more-secrets")
    os.system("make nms")
    os.system("sudo make install")
print("Script complete!")
