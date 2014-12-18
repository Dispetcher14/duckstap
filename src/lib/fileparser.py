#!/usr/bin/env python3

# Parser.
# Can be used just with number of string.
# Already returns number of next string.

from . import staplerops, outputter

class fileparser:
    def __init__(self):
        a=0
        
    def parsestring(self, string):
        if string[0] == '$':
            staplerops.stap(string.split("(")[1][:-1], string.split("(")[2][:-1])
        if string[0] == '#':
            staplerops.diez(string.split("(")[:-1], string.split("<")[:-1])
        if string[0] == '[':
            outputter.tocons(string[1:-1])
        
        return self.get_next_string()
    
    def get_next_string(self, optype):
        a = 0
