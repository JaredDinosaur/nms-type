#!/bin/bash
echo This script must be run as root or with sudo privileges.
echo This script requires git, gcc and make.
echo Press Enter to continue or Ctrl+C to exit...
read

clear
echo Checking if yay is installed...
yay -h > check.yay
if [ "`cat check.yay`" == "" ]; then
    echo yay not found. Using standard installation methods...
    sleep 2
    git clone https://github.com/bartobri/no-more-secrets.git
    cd no-more-secrets
    make nms
    sudo make install
else
    echo Installing packages using yay...
    yay -S no-more-secrets
fi
echo
echo Installation complete!
echo