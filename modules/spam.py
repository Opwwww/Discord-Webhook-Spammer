#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests as r
import time as t
from colorama import Fore as f
from os import system
from time import sleep
import signal
from pystyle import *
from config import *
from sys import platform
if platform == "win32":
 system('title "Webhook Spammer || Discord Webhook Spammer')
elif platform == "linux" or platform == "linux2":
    print()
elif platform == "darwin":
    print()
system("cls || clear")
c = t.ctime()
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
sleep(1)
print(f.BLUE + "[" + f.CYAN + c.split(" ")[3] + f.BLUE + f.GREEN + "]" + f.LIGHTMAGENTA_EX + "[" + f.LIGHTGREEN_EX + "DATA" + f.LIGHTMAGENTA_EX + "]" + f.LIGHTGREEN_EX+"["+f.LIGHTRED_EX+"*"+ f.LIGHTGREEN_EX+ "]"+ f.LIGHTRED_EX+ " Succes loaded webhook spammer.  ")
sleep(1)
#Webhook
print(f.BLUE + "[" + f.CYAN + c.split(" ")[3] + f.BLUE + f.GREEN + "]" + f.LIGHTMAGENTA_EX + "[" + f.LIGHTGREEN_EX + "DATA" + f.LIGHTMAGENTA_EX + "]" + f.LIGHTGREEN_EX+"["+f.LIGHTRED_EX+"*"+ f.LIGHTGREEN_EX+ "]"+ f.LIGHTRED_EX+ " Checking webhook..  ")
c = t.ctime()
webhook_check = r.get(webhook)
c = t.ctime()
if webhook_check.status_code == 404:
 print(f.BLUE + "[" + f.CYAN + c.split(" ")[3] + f.BLUE + f.GREEN + "]" + f.LIGHTMAGENTA_EX + "[" + f.LIGHTGREEN_EX + "CRITICAL" + f.LIGHTMAGENTA_EX + "]" + f.LIGHTGREEN_EX+"["+f.LIGHTRED_EX+"-"+ f.LIGHTGREEN_EX+ "]"+ f.LIGHTRED_EX+ " Failed to connect to  "
 + f.RED + webhook)
 print(f.BLUE + "[" + f.CYAN + c.split(" ")[3] + f.BLUE + f.GREEN + "]" + f.LIGHTMAGENTA_EX + "[" + f.LIGHTGREEN_EX + "CRITICAL" + f.LIGHTMAGENTA_EX + "]" + f.LIGHTGREEN_EX+"["+f.LIGHTRED_EX+"-"+ f.LIGHTGREEN_EX+ "]"+ f.LIGHTRED_EX+ " Check config.py and change your webhook. ")
 exit()
else:
    print(f.BLUE + "[" + f.CYAN + c.split(" ")[3] + f.BLUE + f.GREEN + "]" + f.LIGHTMAGENTA_EX + "[" + f.LIGHTGREEN_EX + "DATA" + f.LIGHTMAGENTA_EX + "]" + f.LIGHTGREEN_EX+"["+f.LIGHTRED_EX+"+"+ f.LIGHTGREEN_EX+ "]"+ f.LIGHTRED_EX+ " Working webhook,starting in 10 seconds.. ")
    sleep(5*2)
def black(req):
    global count
    count += 1
    req.headers['X-Seq-Count'] = count
    return req
count = 0
s = r.Session()
s.auth = black
print(f.BLUE + "[" + f.CYAN + c.split(" ")[3] + f.BLUE + f.GREEN + "]" + f.LIGHTMAGENTA_EX + "[" + f.LIGHTGREEN_EX + "DATA" + f.LIGHTMAGENTA_EX + "]" + f.LIGHTGREEN_EX+"["+f.LIGHTRED_EX+"+"+ f.LIGHTGREEN_EX+ "]"+ f.LIGHTRED_EX+ " STARTING..  ")
while True:
 c = t.ctime()
 while True:
  start_time = t.time()
  yeah = r.get(webhook)
  c = t.ctime()
  start_time = t.time()
  c = t.ctime()
  print(f.BLUE + "[" + f.CYAN + c.split(" ")[3] + f.BLUE + f.GREEN + "]" + f.LIGHTMAGENTA_EX + "[" + f.LIGHTGREEN_EX + "DATA" + f.LIGHTMAGENTA_EX + "]" + f.LIGHTGREEN_EX+"["+f.LIGHTRED_EX+"+"+ f.LIGHTGREEN_EX+ "]"+ f.LIGHTRED_EX+ " STATUS CODE:  " + f.RED + str(yeah.status_code))
  print()
  print(f.BLUE + "[" + f.CYAN + c.split(" ")[3]  + f.BLUE + "]" + f.LIGHTMAGENTA_EX + "[" + f.LIGHTGREEN_EX + "DATA" + f.LIGHTMAGENTA_EX + "]" + f.LIGHTGREEN_EX+"["+f.LIGHTRED_EX + "+" + f.LIGHTGREEN_EX+ "]"+ f.LIGHTRED_EX+ " SPAMMING  " + f.RED + webhook)
  print()
  print(f.BLUE + "[" + f.CYAN + c.split(" ")[3] + f.BLUE + "]" + f.LIGHTMAGENTA_EX + "[" + f.LIGHTGREEN_EX + "DATA" + f.LIGHTMAGENTA_EX + "]" + f.LIGHTGREEN_EX+"["+f.LIGHTRED_EX + "+" + f.LIGHTGREEN_EX+ "]"+ f.LIGHTRED_EX+ " MESSAGE:  " + f.RED + message)
  print()
  print(f.BLUE + "[" + f.CYAN + c.split(" ")[3] + f.BLUE + "]" + f.LIGHTMAGENTA_EX + "[" + f.LIGHTGREEN_EX + "DATA" + f.LIGHTMAGENTA_EX + "]" + f.LIGHTGREEN_EX+"["+f.LIGHTRED_EX + "+" + f.LIGHTGREEN_EX + "]"+ f.LIGHTRED_EX+ " TOTAL MESSAGES:  " + f.RED + str(count))
  print()
  t.sleep(3)
  r.post(webhook,headers=headers,json=data,proxies=proxy,auth=black)
  r.post(webhook,headers=headers,json=data,proxies=proxy,auth=black)
  r.post(webhook,headers=headers,json=data,proxies=proxy,auth=black)
  r.post(webhook,headers=headers,json=data,proxies=proxy,auth=black)
  r.post(webhook,headers=headers,json=data,proxies=proxy,auth=black)
  r.post(webhook,headers=headers,json=data,proxies=proxy,auth=black)
  r.post(webhook,headers=headers,json=data,proxies=proxy,auth=black)
  r.post(webhook,headers=headers,json=data,proxies=proxy,auth=black)
  def handler(signum, frame):
    ye = input(f.BLUE + "[" + f.CYAN + c.split(" ")[3]  + f.BLUE + "]" + f.LIGHTMAGENTA_EX + "[" + f.LIGHTGREEN_EX + "DATA" + f.LIGHTMAGENTA_EX + "]" + f.LIGHTGREEN_EX+"["+f.LIGHTRED_EX + "-" + f.LIGHTGREEN_EX+ "]"+ f.LIGHTRED_EX+ " Do you want to exit? y/n  ")
    if ye == "y" or ye == "ye" or ye == "yes":
     c = t.ctime()
    print(f.BLUE + "[" + f.CYAN + c.split(" ")[3]  + f.BLUE + "]" + f.LIGHTMAGENTA_EX + "[" + f.LIGHTGREEN_EX + "DATA" + f.LIGHTMAGENTA_EX + "]" + f.LIGHTGREEN_EX+"["+f.LIGHTRED_EX + "*" + f.LIGHTGREEN_EX+ "]"+ f.LIGHTRED_EX+ " Total Messages Sent  " + f.RED + str(count))
    print(f.BLUE + "[" + f.CYAN + c.split(" ")[3]  + f.BLUE + "]" + f.LIGHTMAGENTA_EX + "[" + f.LIGHTGREEN_EX + "DATA" + f.LIGHTMAGENTA_EX + "]" + f.LIGHTGREEN_EX+"["+f.LIGHTRED_EX + "*" + f.LIGHTGREEN_EX+ "]"+ f.LIGHTRED_EX+ " Sent it as:   " + f.RED + user)
    print(f.BLUE + "[" + f.CYAN + c.split(" ")[3]  + f.BLUE + "]" + f.LIGHTMAGENTA_EX + "[" + f.LIGHTGREEN_EX + "DATA" + f.LIGHTMAGENTA_EX + "]" + f.LIGHTGREEN_EX+"["+f.LIGHTRED_EX + "*" + f.LIGHTGREEN_EX+ "]"+ f.LIGHTRED_EX+ " Total Time taken:  " + f.RED + "--- %s seconds ---" % (t.time() - start_time))
    print(f.BLUE + "[" + f.CYAN + c.split(" ")[3]  + f.BLUE + "]" + f.LIGHTMAGENTA_EX + "[" + f.LIGHTGREEN_EX + "DATA" + f.LIGHTMAGENTA_EX + "]" + f.LIGHTGREEN_EX+"["+f.LIGHTRED_EX + "-" + f.LIGHTGREEN_EX+ "]"+ f.LIGHTRED_EX+ " Exitting..  ")
    system('cd .. && cmd /k "python main.py" ')
    if ye == "n" or ye == "no":
        sleep(1)
  signal.signal(signal.SIGINT, handler)
  if yeah.status_code == 404:
    c = t.ctime()
    print(f.BLUE + "[" + f.CYAN + c.split(" ")[3]  + f.BLUE + "]" + f.LIGHTMAGENTA_EX + "[" + f.LIGHTGREEN_EX + "CRITICAL" + f.LIGHTMAGENTA_EX + "]" + f.LIGHTGREEN_EX+"["+f.LIGHTRED_EX + "-" + f.LIGHTGREEN_EX+ "]"+ f.LIGHTRED_EX+ " Failed to connect to webhook.  ")
    print(f.BLUE + "[" + f.CYAN + c.split(" ")[3]  + f.BLUE + "]" + f.LIGHTMAGENTA_EX + "[" + f.LIGHTGREEN_EX + "ATTEMPT" + f.LIGHTMAGENTA_EX + "]" + f.LIGHTGREEN_EX+"["+f.LIGHTRED_EX + "*" + f.LIGHTGREEN_EX+ "]"+ f.LIGHTRED_EX+ " Trying to reconnect..  ")
    r.post(webhook,headers=headers,json=data,proxies=proxy,auth=black)
    sleep(3)
    print(f.BLUE + "[" + f.CYAN + c.split(" ")[3]  + f.BLUE + "]" + f.LIGHTMAGENTA_EX + "[" + f.LIGHTGREEN_EX + "CRITICAL" + f.LIGHTMAGENTA_EX + "]" + f.LIGHTGREEN_EX+"["+f.LIGHTRED_EX + "-" + f.LIGHTGREEN_EX+ "]"+ f.LIGHTRED_EX+ " Webhook has been deleted,exitting... ")
    sleep(5)
    print(f.GREEN + "[" + c.split(" ")[3]  + "]" + f.MAGENTA + " [DATA] " + f.RED + " [*] Total Messages Sent: " + str(count))
    print(f.GREEN + "[" + c.split(" ")[3]  + "]" + f.MAGENTA + " [DATA] " + f.RED + " [*] Sent it as: " + user )
    print(f.GREEN + "[" + c.split(" ")[3]  + "]" + f.MAGENTA + " [DATA] " + f.RED + " [*] Total time taken: " + "--- %s seconds ---" % (t.time() - start_time))
    break
 c = t.ctime()
 y = input(f.BLUE + "[" + f.CYAN + c.split(" ")[3]  + f.BLUE + "]" + f.LIGHTMAGENTA_EX + "[" + f.LIGHTGREEN_EX + "DATA" + f.LIGHTMAGENTA_EX + "]" + f.LIGHTGREEN_EX+"["+f.LIGHTRED_EX + "-" + f.LIGHTGREEN_EX+ "]"+ f.LIGHTRED_EX+ " Do you want to restart? y/n  ")
 if y == "y" or y == "yes" or y == "ye":
         system('cd .. && python main.py')
 if y == "n" or y == "no":
     exit() 