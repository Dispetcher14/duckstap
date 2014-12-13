#!/usr/bin/env python3

# Parser.
# Can be used just with number of string.
# Already returns number of next string.

import staplerops, outputter

class fileparser:
    def __init__(self):
        
    def parsestring(self, string):
        if string[0] == '$':
            tocalc(string.split("(")[1][:-1], string.split("(")[2][:-1])
        if string[0] == '#':
            todiez(string.split("(")[:-1], string.split("<")[:-1])
        if string[0] == '[':
            toprint(string[1:-1])
        
        return self.get_next_string
    
    def get_next_string(self):
        """ """
