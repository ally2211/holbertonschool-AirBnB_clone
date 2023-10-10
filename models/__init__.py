#!/usr/bin/python3
import os
from .engine.file_storage import FileStorage


storage = FileStorage()
# If the JSON file exists, call the reload method to load objects
#if os.path.exists(FileStorage._FileStorage__file_path):
storage.reload()
