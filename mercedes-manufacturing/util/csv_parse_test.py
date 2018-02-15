# -*- coding: utf-8 -*-

"""
A simple module to test reading from a csv file into a list of lists
"""

from csv_file_util import CsvFileUtil

def main():
    """A simple main to test loading csv files."""
    fileReader = CsvFileUtil()
    
    fileContents = fileReader.get_file_contents("/home/dev/mercedes-green-manufacturing/data/train.csv")
    for line in fileContents:
        print(', '.join(line), end='\n', flush=True)
    
main()