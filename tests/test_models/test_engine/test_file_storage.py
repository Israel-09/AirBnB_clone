#!/usr/bin/python3
'''testing the engine class'''
import os
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    '''testing the file storage'''

    def setUp(self):
        '''setup method'''
        pass
    
    def test_storage_instance(self):
        '''testing if storage is an instance of FileStorage'''
        self.assertTrue(isinstance(storage, FileStorage))

    def test_objects(self):
        '''testing the object attribute'''
        self.assertFalse(hasattr(storage, '__objects'))
        private_attr = f'_{storage.__class__.__name__}__objects'
        self.assertTrue(private_attr in dir(storage))
    
    def test_file_path(self):
        '''testing the file_path attribute'''
        self.assertFalse(hasattr(storage, '__file_path'))
        private_attr = f'_{storage.__class__.__name__}__file_path'
        self.assertTrue(private_attr in dir(storage))

    def test_all_exist(self):
        '''testing if all method exists'''
        self.assertTrue(hasattr(storage, 'all') and
                        callable(storage.all))

    def test_all(self):
        '''testing 'all' method'''
        self.assertTrue(type(storage.all()), dict)
        storage._FileStorage__objects = {}
        self.assertTrue(storage.all() == {})
        model1 = BaseModel()
        model2= BaseModel()
        self.assertEqual(len(storage.all()), 2)

    def test_new_exist(self):
        '''testing if new method exists'''
        self.assertTrue(hasattr(storage, 'new') and
                        callable(storage.new))

    def test_new(self):
        '''testing the new method'''
        obj_len = len(storage.all())
        my_model = BaseModel()
        new_len = len(storage.all())
        self.assertEqual(new_len, obj_len + 1)

    def test_save_exist(self):
        '''testing if save method exists'''
        self.assertTrue(hasattr(storage, 'save') and
                        callable(storage.save))

    def test_save(self):
        '''testing the save method'''
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)
        storage._FileStorage__objects = {}
        new_model = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists(storage._FileStorage__file_path))

    def test_reload_exist(self):
        '''testing if reload method exists'''
        self.assertTrue(hasattr(storage, 'reload') and
                        callable(storage.reload))

    def test_reload(self):
        '''testing the reload method'''
        my_model = BaseModel()
        storage.save()
        storage._FileStorage__objects = {}
        self.assertTrue(storage.all() == {})
        storage.reload()
        self.assertFalse(storage.all() == {})


