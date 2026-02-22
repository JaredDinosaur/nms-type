import os
print("This script must be run as root or a user with sudo privileges.")
print("This script requires the packages git, gcc and make.")
ready=input("Enter 'ready' to run the script, or anything else to cancel: ")
if ready.lower()=="ready":
    os.system("clear")
    print("Checking if yay is installed...")
    os.system("yay -h > check.yay")
    file=open("check.yay","r")
    if file.read() == "":
        print("yay not found. Using standard installation methods...")
        time.sleep(2)
        os.system("git clone https://github.com/bartobri/no-more-secrets.git")
        os.system("cd no-more-secrets && make nms && sudo make install")
    else:
        print("Installing packages using yay...")
        os.system("yay -S no-more-secrets")
    print("Script complete!")
