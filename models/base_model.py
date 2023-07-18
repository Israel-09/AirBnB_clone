#!/usr/bin/python3
'''module that defines common attributes of instances'''
import uuid
from datetime import datetime
import models


class BaseModel:
    '''basemodel class for all other classes'''

    def __init__(self, *args, **kwargs):
        '''class constructor for the base model'''
        if kwargs:
            for attr in kwargs.keys():
                if not attr == '__class__':
                    if attr == 'updated_at' or attr == 'created_at':
                        value = datetime.fromisoformat(kwargs[attr])
                    else:
                        value = kwargs[attr]
                    setattr(self, attr, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        '''saves an instance to a file'''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''returns the key-value of all instance attributes'''
        dict_obj = {}

        dict_obj['__class__'] = self.__class__.__name__

        for attr in self.__dict__.keys():
            if attr == 'updated_at' or attr == 'created_at':
                dict_obj[attr] = self.__dict__[attr].isoformat()
            else:
                dict_obj[attr] = self.__dict__[attr]

        return (dict_obj)

    def __str__(self):
        '''string representation of the class'''
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id,
                                     self.__dict__)
