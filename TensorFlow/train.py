import cv2
import requests 
import uuid
import os
import time
import config
import wget
import object_detection

#Get list of all current perks using DBD API
r = requests.get("http://dbd-api.herokuapp.com/perks?lang=en").json()
perks_list = []

for item in r:
    perks_list.append(item['perk_name'])

for path in config.paths.values():
    if not os.path.exists(path):
        os.mkdir(path)
