#!/usr/bin/python3
'''deserialize the existing instance'''
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
