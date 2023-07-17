#!/usr/bin/python3
'''testing base_model'''
import unittest
from models.base_model import BaseModel


class BaseModelTest(unittest.TestCase):
    '''basemodel test case'''

    def setUp(self):
        self.model1 = BaseModel()
        self.model2 = BaseModel()

    def test_base_model_id(self):
        '''testing the id attribute'''
        self.assertIsInstance(self.model1, BaseModel)
        self.assertTrue(hasattr(self.model1, 'id'))
        self.assertTrue(type(self.model1.id), str)
        self.assertNotEqual(self.model1.id, self.model2.id)

    def test_base_model_created_at(self):
        '''testing the created_at attrinbute'''
        self.assertTrue(hasattr(self.model1, 'created_at'))
        self.assertTrue(type(self.model1.created_at), 'datetime.datetime')

    def test_base_model_updated_at(self):
        '''testing the updated_at attrinbute'''
        self.assertTrue(hasattr(self.model1, 'updated_at'))
        self.assertTrue(type(self.model1.updated_at), 'datetime.datetime')
        self.assertNotEqual(self.model1.created_at, self.model2.created_at)

    def test_base_model_save(self)
        '''testing the save method of BaseModel'''
        self.model1.save()
        
