# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os


def splitFile(fLines,startLine = 31):
    gLines = []
    for idx, line in enumerate(fLines[startLine:]):
        if "exec" in line:
            splitLine = line.split()        
            gLines.append(splitLine)
    return gLines

def processData(data):
    assets = {}
    for asset in data:
        name = os.path.split(asset[5])
        fileType = name[:-3]
        size = expandNotation(asset[2],asset[3])
        path = asset[5]
        assets[path] = {'name':name, 'size':size}
    return assets
        
def expandNotation(size, notation):
    notations = {'mb':1e6, 'kb':1e3 }
    if notation in notations:
        return int(float(size)*notations[notation])
    return size

if __name__ == "__main__":
    f = open("H:/Projects/Tools/python/data/buildLog.txt",'r')
    fLines = f.readlines()
    f.close()
    data = splitFile(fLines)
    print(processData(data))