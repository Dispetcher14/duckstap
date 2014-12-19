#!/usr/bin/env python3

class common:
    arr = {}
    def __init__(self):
        self.readconfig()
        
    def readconfig(self):
        conf_opened = open('../conf/duckstap.conf', 'r')
        for i in conf_opened:
            if i[0] != '#':
                self.arr[i.split(': ')[0]] = i.split(': ')[1]
    
