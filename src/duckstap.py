#!/usr/bin/env python3

from lib import staplermath
from lib import fileparser
from lib import common

fileparse = fileparser.fileparser.parsestring

class duckstap:
    def __init__(self):
        self.filename = input()
        self.common_arr = common.common.arr
        print(self.common_arr)
        
    def file_parse(self):
        flong = 0
        for i in self.filename:
            flong += 1

        infile = 0
        
        while infile < (self.flong-1):
            infile = fileparse(infile)

