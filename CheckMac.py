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

def menu():
    os.system("clear")
    time.sleep(3)
    print(f"{red}***************************")
    print(f"{white}* [ Author : Deauther   ] *")
    print(f"{red}* [ Wi-fi Address Check ] *")
    print(f"{white}* [1] Mac Check           *")
    print(f"{red}* [0] Exit                *")
    print("***************************")
    tools = input(f"""{white}Input Number: """)

    if tools="1":
       os.system("clear")
       time.sleep(3)
       os.system("iwconfig")
       time.sleep(3)
       os.system("clear")
       os.system("airmon-ng start wlan0")
       time.sleep(3)
       os.system("clear")
       os.system("airodump-ng start wlan0")
       print("""Copy Mac Wi-fi And Paste In nano Deauthertest.py, Cancel Command CTRL + C.""")

    elif tools="0":
       os.system("clear")
       print("Byee...See You Again.")
       time.sleep(3)
       os.system("clear")
       sys.exit()

    else:
       os.system("clear")
       print("Pls Input Code Valid...!!!")
       time.sleep(3)
       os.system("python CheckMac.py")

menu()
