#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from threading import Thread
from config import *
import requests as r
from colorama import Fore as f
from os import system
from time import sleep 
from pystyle import * 
import time
from sys import platform
if platform == "win32":
 system('title "Webhook Spammer V2 || Discord Webhook Spammer')
elif platform == "linux" or "linux2":
    print()
elif platform == "darwin":
    print()
c = time.ctime()
system("cls || clear")
Write.Print("""
'##:::::'##:'########:'########::'##::::'##::'#######:::'#######::'##:::'##::'######::'########:::::'###::::'##::::'##:'##::::'##:'########:'########::
 ##:'##: ##: ##.....:: ##.... ##: ##:::: ##:'##.... ##:'##.... ##: ##::'##::'##... ##: ##.... ##:::'## ##::: ###::'###: ###::'###: ##.....:: ##.... ##:
 ##: ##: ##: ##::::::: ##:::: ##: ##:::: ##: ##:::: ##: ##:::: ##: ##:'##::: ##:::..:: ##:::: ##::'##:. ##:: ####'####: ####'####: ##::::::: ##:::: ##:
 ##: ##: ##: ######::: ########:: #########: ##:::: ##: ##:::: ##: #####::::. ######:: ########::'##:::. ##: ## ### ##: ## ### ##: ######::: ########::
 ##: ##: ##: ##...:::: ##.... ##: ##.... ##: ##:::: ##: ##:::: ##: ##. ##::::..... ##: ##.....::: #########: ##. #: ##: ##. #: ##: ##...:::: ##.. ##:::
 ##: ##: ##: ##::::::: ##:::: ##: ##:::: ##: ##:::: ##: ##:::: ##: ##:. ##::'##::: ##: ##:::::::: ##.... ##: ##:.:: ##: ##:.:: ##: ##::::::: ##::. ##::
. ###. ###:: ########: ########:: ##:::: ##:. #######::. #######:: ##::. ##:. ######:: ##:::::::: ##:::: ##: ##:::: ##: ##:::: ##: ########: ##:::. ##:
:...::...:::........::........:::..:::::..:::.......::::.......:::..::::..:::......:::..:::::::::..:::::..::..:::::..::..:::::..::........::..:::::..::
""",Colors.red_to_black,interval=0.01)
sleep(2)
c = time.ctime()
print(f.BLUE + "[" + f.CYAN + c.split(" ")[3]  + f.BLUE + "]" + f.LIGHTMAGENTA_EX + "[" + f.LIGHTGREEN_EX + "DATA" + f.LIGHTMAGENTA_EX + "]" + f.LIGHTGREEN_EX+"["+f.LIGHTRED_EX + "+" + f.LIGHTGREEN_EX+ "]"+ f.LIGHTRED_EX+ " Sending messages.. ")
def black():
    while True:
     r.post(webhook,headers=headers,json=data)
while True:
    while True:
     yes = r.get(webhook)
     if yes.status_code == 404:
        print(f.RED+"[-] Invalid webhook")
        sleep(5)
        system('cd .. && cmd /k "python main.py" ')
     if yes.status_code == 200:
      thread = Thread(target=black)
      thread.start()
      thread.join()
      break
#nigger