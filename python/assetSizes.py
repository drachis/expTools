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
            splitLine = line.split(None,5)        
            gLines.append(splitLine)
    return gLines

def processData(data):
    assets = {}
    for asset in data:
        path, name = os.path.split(asset[5])
        fileType = None
        if "." in name:
            fileType = name.split(".")[1].strip()
        size = expandNotation(asset[2],asset[3])
        percent = asset[4]
        path = asset[5]
        if fileType != None:
            assets[path] = {'name':name,
                        'size':size,
                        'extension':fileType,
                        'percent':percent,
                        'path':path}
    return assets

def sortByKey(assets, key):
    byExt = {}
    for _key in assets:
        asset = assets[_key]
        if asset[key] != None:
            if asset[key] not in byExt:
                byExt[asset[key]] = [asset]
            if asset[key] in byExt:
                byExt[asset[key]].append(asset)
    return byExt

def sizeByKey(byType):
    for _type in byType:
        sizeSum = 0
        for elem in byType[_type]:
            sizeSum += elem['size']
        print(_type, "{:,}".format(sizeSum))

def filterOutValue(assets, value):
    filtered = {}
    for _key in assets:
        key = _key
        if value not in key:
            filtered[key] = assets[key]
    return filtered
    
def expandNotation(size, notation):
    notations = {'mb':1048576, 'kb':1024 }
    if notation in notations:
        return int(float(size)*notations[notation])
    return size

if __name__ == "__main__":
    f = open("data/buildLog.txt",'r')
    fLines = f.readlines()
    f.close()
    data = splitFile(fLines)
    #processed = processData(data)
    #sizeByKey(sortByKey(processed,"extension"))
    noExternal = filterOutValue(processed, "ExternalTextures")
    sizeByKey(sortByKey(noExternal,"extension"))
