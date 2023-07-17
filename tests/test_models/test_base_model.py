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
        self.assertNotEqual(self.model1.created_at, self.model2.created_at)

    def test_base_model_updated_at(self):
        '''testing the updated_at attrinbute'''
        self.assertTrue(hasattr(self.model1, 'updated_at'))
        self.assertTrue(type(self.model1.updated_at), 'datetime.datetime')
        self.assertNotEqual(self.model1.created_at, self.model1.updated_at)

    def test_base_model_save(self):
        '''testing the save method of BaseModel'''
        self.assertTrue(hasattr(self.model1, 'save') and
                        callable(self.model1.save))
        current_time = self.model1.updated_at
        self.model1.save()
        self.assertNotEqual(current_time, self.model1.updated_at)

    def test_base_model_to_dict(self):
        '''testing the to_dict method of BaseModel'''
        self.assertTrue(hasattr(self.model1, 'to_dict') and
                        callable(self.model1.to_dict))
        self.assertNotEqual(self.model1.to_dict, self.__dict__)
        dict_obj = self.model1.to_dict()
        self.assertTrue('__class__' in dict_obj)
        self.assertTrue('id' in dict_obj)
        self.assertTrue('created_at' in dict_obj)
        self.assertTrue('updated_at' in dict_obj)
        dt_format = self.model1.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        self.assertEqual(dict_obj['created_at'], dt_format)
        dt_format = self.model1.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        self.assertEqual(dict_obj['updated_at'], dt_format)

    def test_base_str(self):
        '''testing the __str__ method'''
        str_rep = '[{}] ({}) {}'.format(self.model1.__class__.__name__,
                                        self.model1.id,
                                        self.model1.__dict__
                                        )
        self.assertEqual(str_rep, str(self.model1))
        self.assertEqual(str_rep, self.model1)
