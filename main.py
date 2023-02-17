#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from colorama import Fore as f
from os import system as opw
from pystyle import * 
import time
import requests
from sys import platform
if platform == "win32":
 setTitle = opw("title Discord Webhook Spammer [opw#7777]")
 setTitle
elif platform == "linux" or platform == "linux2":
   alr = opw("python3 main.py")
opw("cls || clear")
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
print()
time.sleep(1)
print(f.LIGHTGREEN_EX+"["+f.LIGHTRED_EX+"*"+ f.LIGHTGREEN_EX+ "]"+ f.LIGHTRED_EX+ " Made By opw#7777 ")
print()
print(f.LIGHTGREEN_EX+"["+f.LIGHTRED_EX+"*"+ f.LIGHTGREEN_EX+ "]"+ f.LIGHTRED_EX+ " Type Help For more information ")
print()
print(f.LIGHTGREEN_EX+"["+f.LIGHTRED_EX+"1"+ f.LIGHTGREEN_EX+ "]"+ f.LIGHTRED_EX+ " Webhook Spammer ")
print()
print(f.LIGHTGREEN_EX+"["+f.LIGHTRED_EX+"2"+ f.LIGHTGREEN_EX+ "]"+ f.LIGHTRED_EX+ " Webhook Spammer V2")
print()
print(f.LIGHTGREEN_EX+"["+f.LIGHTRED_EX+"3"+ f.LIGHTGREEN_EX+ "]"+ f.LIGHTRED_EX+ " Webhook Checker")
print()
print(f.LIGHTGREEN_EX+"["+f.LIGHTRED_EX+"4"+ f.LIGHTGREEN_EX+ "]"+ f.LIGHTRED_EX+ " Webhook Deleter.")
print()
print(f.LIGHTGREEN_EX+"["+f.LIGHTRED_EX+"5"+ f.LIGHTGREEN_EX+ "]"+ f.LIGHTRED_EX+ " Magic Command.")
while True:
 print()
 c = time.ctime() 
 yes = input(f.BLUE + "[" + f.GREEN + c.split(" ")[3]+ f.BLUE + "]"+f.BLUE + "[" + f.GREEN + ">>>" +  f.BLUE + "] ")
 if yes == "1" or yes == "01":
    opw('cd Modules && python spam.py ')
 if yes == "2" or yes == "02":
    opw('cd Modules && python spamv2.py ')
 if yes == "3" or yes == "03":
    opw('cd Modules && python checker.py ')
 if yes == "4" or yes == "04":
   web = input("Webhook: ")
   requests.delete(web)
   print(f.BLUE + "[" + f.GREEN + c.split(" ")[3] + f.BLUE + "]"+ f.BLUE + f.LIGHTBLUE_EX + f.BLUE + "[" + f.GREEN + ">>>" +  f.BLUE + "]" + "[" + f.CYAN + "+" + f.LIGHTBLUE_EX + "]" + f.GREEN + " Done")
 if yes == "5" or yes == "05" or yes == "secret" or yes == "-":
    opw('cd Modules && python magic.py ')
 if yes == "help" or yes == "Help" or yes == "HELP" or yes == "HELp":
   opw('cmd /k "python main.py" ') & alr
   if yes == "credits":
      print(f.BLUE + "[" + f.GREEN + c.split(" ")[3] + f.BLUE + "]"+ f.LIGHTCYAN_EX + """
      Made by opw#7777

      Time thing by wack the beaner    

      """)

   print(f.BLUE + "[" + f.GREEN + c.split(" ")[3] + f.BLUE + "]"+ f.RED+"""
   First command (Webhook Spammer) its a webhook spammer that uses requests and loop (Its slow)
   
   Second command is faster but discord will rate limit you and you will not be able to use discord for some hours.
   
   Third command is to check the webhook status you can change it on "config.py")
   """)
   yes = input(f.BLUE + "[" + f.GREEN + c.split(" ")[3]+ f.BLUE + "]"+f.BLUE + "[" + f.GREEN + ">>>" +  f.BLUE + "] ")
 else:
   yes = input(f.BLUE + "[" + f.GREEN + c.split(" ")[3]+ f.BLUE + "]"+f.BLUE + "[" + f.GREEN + ">>>" +  f.BLUE + "] ")
