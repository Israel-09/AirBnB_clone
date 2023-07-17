#!/usr/bin/python3
'''module that defines common attributes of instances'''
import uuid
from datetime import datetime


class BaseModel:
    '''basemodel class for all other classes'''

    def __init__(self):
        '''class constructor for the base model'''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        '''saves an instance to a file'''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''returns the key-value of all instance attributes'''
        dict_obj = {}

        dict_obj['__class__'] = self.__class__.__name__
        
        for attr in self.__dict__.keys():
            dict_obj[attr] = self.__dict__[attr]

        print(dict_obj)

    def __str__(self):
        '''string representation of the class'''
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id,
                                     self.__dict__)


base = BaseModel()
base.to_dict()
