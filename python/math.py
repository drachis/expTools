# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 11:46:27 2014

@author: toli
"""
import math

def toPowTwo(value):
    a = math.log(value)/math.log(2)
    b = math.floor(a)
    if(a==b):
        return value
    else:
        if (a-b) < 0.5:
            return math.pow(2,b)
        else:
                return math.pow(2,b+1)

if __name__ == "__main__":
    print toPowTwo(150)