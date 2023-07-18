#!/usr/bin/python3
from models import storage
import os
from models.base_model import BaseModel

if os.path.exists('file.json'):
    os.remove('file.json')
else:
    print('unavailable')
'''all_objs = storage.all()
my_model = BaseModel()
print(len(storage.all()) == 1)
'''
'''
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)
'''
