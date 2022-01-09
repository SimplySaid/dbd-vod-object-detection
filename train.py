import cv2
import requests 
import uuid
import os
import time

#Get list of all current perks using DBD API
r = requests.get("http://dbd-api.herokuapp.com/perks?lang=en").json()
perks_list = []

for item in r:
    perks_list.append(item['perk_name'])

PERKS_PATH = os.path.join('Tensorflow', 'perks', 'collectedperks')

if not os.path.exists(PERKS_PATH):
    os.makedirs(PERKS_PATH)
for perk in perks_list:
    path = os.path.join(PERKS_PATH, perk)
    if not os.path.exists(path):
        os.makedirs(path)

