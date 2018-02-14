#!/usr/bin/env python 3

""" 
A module defining an abstract class for reading from a file (CSV for instance)
into data structures and from data into a file.
"""

__author__ = "Bryan Anders"
__copyright__ = "Copyright 2018, Bryan Anders"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Bryan Anders"
__email__ = "bryaneanders@gmail.com"

import abc
import logging

class FileUtil:
    __metaclass__ = abc.ABCMeta


    def __init__(self):
        self.logger = logging.getLogger();
    
    @abc.abstractmethod
    def get_file_contents(self, path):
        """Defines the template for retrieving the contents of a file."""
        
        return
    
    @classmethod
    def __subclasshook__(cls):
        """Checks if a class object is an instance of FileUtil."""
        
        return isinstance(cls, FileUtil)