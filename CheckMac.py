#!bin/python

# Import Python Package
import os, sys, time
import random

# Color Text
green  = "\033[1;92m"
white  = "\033[1;97m"
ash    = "\033[1;90m"
yellow = "\033[1;93m"
purple = "\033[1;95m"
red    = "\033[1;91m"
blue   = "\033[1;96m"

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
    os.system("clear")
    time.sleep(3)
    textwalk(f"{red}Hello welcome CheckMac\n{green}don't forget follow my @github\n{red}@peopleuniversal \n{green}Thank You...!!!")
    os.system("clear")
    print(f"{red}***************************")
    print(f"{red}* [ Author : Deauther   ] *")
    print(f"{red}* [ Wi-fi Address Check ] *")
    print(f"{ash}* [1] Mac Check           *")
    print(f"{ash}* [0] Exit                *")
    print(f"{ash}***************************")
    tools = input(f"""{ash}Input Number > """)

    # Output
    if tools == "1":
        print(f"{green}")
        os.system("clear")
        time.sleep(3)
        os.system("iwconfig")
        time.sleep(3)
        os.system("clear")
        os.system("airmon-ng start wlan0")
        time.sleep(3)
        os.system("clear")
        print("Cancel Command CTRL + C")
        time.sleep(4)
        os.system("airodump-ng wlan0")
        print(f"{red}Copy Mac Wi-fi And Paste In nano Deauthertest.py")

    # Output Exit
    elif tools == "0":
        os.system("clear")
        print(f"{red}Byee...!!!")
        time.sleep(3)
        os.system("clear")
        time.sleep(2)
        sys.exit()

    # Output Error
    else:
        os.system("clear")
        print(f"{red}Pls Input {green}Code Valid...!!!")
        time.sleep(3)
        os.system("python CheckMac.py")
menu()
