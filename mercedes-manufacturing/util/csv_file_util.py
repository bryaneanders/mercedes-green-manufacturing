# -*- coding: utf-8 -*-

""" 
A module defining a class for reading from a CSV file and returning its 
contents as a list of lists.
"""

__author__ = "Bryan Anders"
__copyright__ = "Copyright 2018, Bryan Anders"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Bryan Anders"
__email__ = "bryaneanders@gmail.com"

import os
from file_util import FileUtil

class CsvFileUtil(FileUtil):
    
    def __init(self):
        """Calls the super init method"""
        
        super(self).__init__()
    
    
    def get_file_contents(self, path):
        """Parses a csv file into a list of lists to return.
        
        Takes the path string as a parameter 
        
        Returns an empty list of no path is provided, the path does not 
        correspond to a file on the filesystem or the file is empty.
        
        """
        
        # The path string must exist
        if not path:
            self.logger.warning(
                    "CsvFileUtil.get_file_contents - No path specifed")
            return []
        
        # The file the path points to must exist
        if not os.path.isfile(path):
            self.logger.error("CsvFileUtil.get_file_contents - Path " 
                              + path + " does not correspond to a file")
            return []
        
        # Load the file and parse its contents
        with open(path) as file:
            content = file.readlines()
            
       
        content =  [line.strip().split() for line in content]
        
        #self.logger.debug("File contents: " + os.linesep + content)
        #print("File contents: " + os.linesep + content)
        return content
        
        
            
        
            