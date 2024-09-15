#!bin/python

import os, sys, time

def menu():
    os.system("clear")
    time.sleep(3)
    print("***************************")
    print("* [ Author : Deauther   ] *")
    print("* [ Wi-fi Address Check ] *")
    print("* [1] Mac Check           *")
    print("* [0] Exit                *")
    print("***************************")
    tools = input("""Input Number > """)

    if tools="1":
       os.system("clear")
       time.sleep(3)
       os.system("iwconfig")
       time.sleep(3)
       os.system("clear")
       os.system("airmon-ng start wlan0")
       time.sleep(3)
       os.system("clear")
       os.system("airmon-ng check kill")
       time.sleep(3)
       os.system("clear")
       os.system("airodump-ng start wlan0")
       print("Copy Mac Wi-fi And Paste In nano Deauthertest.py")
       print("Cancel Command CTRL + C")

    elif tools="0":
       os.system("clear")
       print("Byee...!!!")
       time.sleep(3)
       os.system("clear")
       time.sleep(2)
       sys.exit()

    else:
       os.system("clear")
       print("Pls Input Code Valid...!!!")
       time.sleep(3)
       os.system("python CheckMac.py")
       
menu()
