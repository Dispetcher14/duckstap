#!/usr/bin/env python3

from lib import staplermath
from lib import fileparser

fileparse = fileparser.parsestring

class duckstap:
    def __init__(self):
        self.filename = input()
        
    def file_parse(self):
        flong = 0
        for i in self.filename:
            flong += 1

        infile = 0
        
        while infile < (self.flong-1):
            infile = fileparse(infile)
