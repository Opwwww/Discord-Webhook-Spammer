#!/usr/bin/env bash
# -*- coding: utf-8 -*-
if (( $(id -u) == 0 )); then
    echo "installing modules.." && pip install -r requirements.txt && python3 main.py
else 
sudo pip install -r requirements.txt && python3 main.py
fi
