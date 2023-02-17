#!/usr/bin/env bash
# -*- coding: utf-8 -*-
echo "do you want to update? y/n"
read -r restart
if [[ $restart == "y" ]]; then
    sudo rm -r Discord-Webhook-Spammer && git clone https://gtithub.com/opwwww/Discord-Webhook-Spammer
else 
    bash start.sh
fi