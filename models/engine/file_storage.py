#!/usr/bin/python3
'''module for serialozation and deserialization
for objects for storage'''
'''from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User'''
from models.base_model import BaseModel
from json import loads, dumps

class FileStorage:
    '''class to serialize and deserialize instances'''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''returns the stored objects'''
        return self.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        obj_key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[obj_key] = obj.to_dict()

    def save(self):
        '''serialize the instances to a file'''
        json_obj = dumps(self.__objects)
        try:
            with open(self.__file_path, 'w', encoding='utf-8') as f:
                f.write(json_obj)
        except FileNotFoundError:
            pass

    def reload(self):
        '''deserialize the instance in a file'''
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                json_obj = f.read()
                if not json_obj or json_obj == '':
                    self.__objects = {}
                else:
                    instances = loads(json_obj)
                    for k in instances.keys():
                        model = BaseModel(**instances[k])
                        self.new(model)
                        
        except FileNotFoundError:
            pass
        
