from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint
import random
from pathlib import Path
import os
from collections import namedtuple

'''
client = MongoClient('mongodb://localhost:27017/')
db = client['BotVK_dudiesWithLOVE']
db = db.series
for doc in db.find():
    pprint.pprint(doc)
'''
def different_names(name):
    ls = ['shawty', 'tati', 'bae', 'babe']
    if name.lower() == 'анастасия':
        ls.append('настя')
        return 'настя'
    if name.lower() == 'екатерина':
        ls.append('катя')
        return 'катя'
    else:
        ls.append(name)
    nm = random.choice(ls)
    return name


def image_add_text(id, number_of_photo=1, text='Sample_text', x=0, y=0, size=36, color=(0,0,0)):
    img = Image.open(f"temple_photo/{number_of_photo}.jpg")
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype(font='/home/san/PycharmProjects/BotVK_dudiesWithLOVE/AlibabaSans-Heavy.otf', size=size, encoding='unic')
    # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((x, y), text, color, font=font)

    if not os.path.exists(f'vk_id_{id}'):
        os.makedirs(f'vk_id_{id}',)
    path = f'vk_id_{id}/photo_{number_of_photo}.jpg'
    img.save(path)
    return path

dict_of_id = {}

def give_photo(id, text='Polina', dict_of_id={}):
    text = different_names(text)
    eleven_meme =False
    ran = 0
    if id in dict_of_id.keys():
        if len(dict_of_id[id]) != 0:
            ls = dict_of_id[id]
            ran = random.choice(ls)
            ls.remove(ran)
            dict_of_id[id] = ls
        else:
            img = image_add_text(id, number_of_photo=11, text=text, x=10050, y=20, size=50)
            eleven_meme = True
            dict_of_id[id] = [x for x in range(1, 11)]
    else:
        dict_of_id[id] = [x for x in range(1, 11)]
        ls = dict_of_id[id]
        ran = random.choice(ls)
        ls.remove(ran)
        dict_of_id[id] = ls

    if ran == 1:
        img = image_add_text(id, number_of_photo=1, text=text, x=450, y=20, size=50)
    if ran == 2:
        img = image_add_text(id, number_of_photo=2, text=text, x=70, y=2, size=50)
    if ran == 3:
        img = image_add_text(id, number_of_photo=3, text=text, x=200, y=200, size=50)
    if ran == 4:
        img = image_add_text(id, number_of_photo=4, text=text, x=650, y=41, size=64, color=(255,255,255))
    if ran == 5:
        img = image_add_text(id, number_of_photo=5, text=text, x=100, y=350, size=64, color=(255,255,255))
    if ran == 6:
        img = image_add_text(id, number_of_photo=6, text=text, x=290, y=80, size=40, color=(255,255,255))
    if ran == 7:
        img = image_add_text(id, number_of_photo=7, text=text, x=450, y=50, size=32)
    if ran == 8:
        img = image_add_text(id, number_of_photo=8, text=text, x=150, y=700, size=64, color=(255,255,255))
    if ran == 9:
        img = image_add_text(id, number_of_photo=9, text=text, x=250, y=41, size=64)
    if ran == 10:
        img = image_add_text(id, number_of_photo=10, text=text, x=50, y=420, size=44, color=(255,255,255))

    return img, eleven_meme








