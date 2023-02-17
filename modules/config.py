#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
#Put your webhook here
webhook = ""
#Username of the webhook
user = "nigger"
#Message of ther webhook
message = "@everyone"
# Put a url of a picture
avatar = ""
#Message,user and avatar of the webhook
data = {
  "content": message,
  "username": user,
  "avatar_url": avatar
}
#Proxy (I dont even use it)
session = requests.Session()
proxy = {
    'http': '78.85.138.22:8081',
    'http': '1.10.133.244:8080',
    'http': '1.10.178.183:8080',
    'http': '123.244.148.14:56609',
    'http': '60.189.127.40:3000',
    'http': '114.239.149.43:9999',
    'http': '171.35.223.240:9999',
    'http': '188.216.179.138:8118',
    'http': '194.193.59.249:8080',
    'http': '115.239.27.40:9999',
    'http': '154.70.98.165:8080'
}
#Check webhook status
status = requests.get(webhook)
#headers
headers = {"Content-Type": "application/json"}
