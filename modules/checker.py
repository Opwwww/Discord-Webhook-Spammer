#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests as r
from colorama import Fore as f
from os import system as opw
from time import sleep 
from pystyle import *
import time
from config import *
from sys import platform
opw("title Webhook Checker || Discord Webhook Spammer")
opw("cls || clear")
c = time.ctime()
n = r.get(webhook).json()
Write.Print("""
'##:::::'##:'########:'########::'##::::'##::'#######:::'#######::'##:::'##::'######::'########:::::'###::::'##::::'##:'##::::'##:'########:'########::
 ##:'##: ##: ##.....:: ##.... ##: ##:::: ##:'##.... ##:'##.... ##: ##::'##::'##... ##: ##.... ##:::'## ##::: ###::'###: ###::'###: ##.....:: ##.... ##:
 ##: ##: ##: ##::::::: ##:::: ##: ##:::: ##: ##:::: ##: ##:::: ##: ##:'##::: ##:::..:: ##:::: ##::'##:. ##:: ####'####: ####'####: ##::::::: ##:::: ##:
 ##: ##: ##: ######::: ########:: #########: ##:::: ##: ##:::: ##: #####::::. ######:: ########::'##:::. ##: ## ### ##: ## ### ##: ######::: ########::
 ##: ##: ##: ##...:::: ##.... ##: ##.... ##: ##:::: ##: ##:::: ##: ##. ##::::..... ##: ##.....::: #########: ##. #: ##: ##. #: ##: ##...:::: ##.. ##:::
 ##: ##: ##: ##::::::: ##:::: ##: ##:::: ##: ##:::: ##: ##:::: ##: ##:. ##::'##::: ##: ##:::::::: ##.... ##: ##:.:: ##: ##:.:: ##: ##::::::: ##::. ##::
. ###. ###:: ########: ########:: ##:::: ##:. #######::. #######:: ##::. ##:. ######:: ##:::::::: ##:::: ##: ##:::: ##: ##:::: ##: ########: ##:::. ##:
:...::...:::........::........:::..:::::..:::.......::::.......:::..::::..:::......:::..:::::::::..:::::..::..:::::..::..:::::..::........::..:::::..::
""",Colors.black_to_white, interval=0.01)
c = time.ctime()
print(f.BLUE + "[" + f.GREEN + c.split(" ")[3]+ f.BLUE + "]"+f.LIGHTGREEN_EX+"["+f.LIGHTRED_EX+"*"+ f.LIGHTGREEN_EX+ "]"+ f.LIGHTRED_EX+ " Checking Webhook...")
status = r.get(webhook)  
sleep(3)
c = time.ctime()
if status.status_code == 404:
    print(f.BLUE + "[" + f.GREEN + c.split(" ")[3]+ f.BLUE + "]"+f.LIGHTGREEN_EX+"["+f.LIGHTRED_EX+"-"+ f.LIGHTGREEN_EX+ "]"+ f.LIGHTRED_EX+ " Invalid webhook.")
    sleep(1)
    opw('cmd /k "python main.py"') 
if status.status_code == 200:
    c = time.ctime()
    print(f.BLUE + "[" + f.GREEN + c.split(" ")[3]  + f.BLUE + "]" + f.LIGHTMAGENTA_EX + "[" + f.LIGHTGREEN_EX + "DATA" + f.LIGHTMAGENTA_EX + "]" + f.LIGHTGREEN_EX+"["+f.LIGHTRED_EX + "+" + f.LIGHTGREEN_EX+ "]"+ f.LIGHTRED_EX+ " Working webook. ")
    sleep(3)
    c = time.ctime()
    print(f.BLUE + "[" + f.GREEN + c.split(" ")[3]  + f.BLUE + "]" + f.LIGHTMAGENTA_EX + "[" + f.LIGHTGREEN_EX + "DATA" + f.LIGHTMAGENTA_EX + "]" + f.LIGHTGREEN_EX+"["+f.LIGHTRED_EX + "+" + f.LIGHTGREEN_EX+ "]"+ f.LIGHTRED_EX+ " Do you want to see the information of the webhook? y/n ")
    c = time.ctime()
    yes = input(f.BLUE + "[" + f.GREEN + c.split(" ")[3]+ f.BLUE + "]"+ f.BLUE + "[" + f.GREEN + ">>>" +  f.BLUE + "] ")
if yes == "Y" or yes == "ye" or yes == "yes" or yes == "y":
    print(f.GREEN + str(n))
if yes == "no" or yes == "n":
    print(f.BLUE + "[" + f.GREEN + c.split(" ")[3]+ f.BLUE + "]"+ f.RED + "Exitting..")
    sleep(1)
    opw('cd .. && cmd /k "python main.py" ')
else:
    yes = input(">>> ")
    opw("color b")
