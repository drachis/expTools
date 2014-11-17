# -*- coding: utf-8 -*-
"""
Created on Thu Nov 06 17:16:02 2014

@author: toli
"""

#http://promo.na.leagueoflegends.com/sru-map-assets/6/47/39.png
import urllib.request
import shutil
import io
from PIL import Image

def downloadImages():
    files = {}
    for h in range(0,47):
        for v in range(0,40):
            filename = ("H:/Projects/Python/Downloaded/new_Sr_{0}_{1}.png".format(h,v))
            
            url = "http://promo.na.leagueoflegends.com/sru-map-assets/6/{0}/{1}.png".format(h,v)
            with urllib.request.urlopen(url) as response, open(filename,'wb') as out_file:
                shutil.copyfileobj(response, out_file)
                files[filename] = out_file
        print( h)
    for filename in files:
        try:
            in_file = Image.save(files[filename])
        except:
            print("cannot save file", filename)
        files[filename].close()

def compositeImage(h, v, files):
    
    image = Image.image.new("RGB", (h,v) ,"Black")
    
 
if __name__ == "__main__":
    downloadImages()

    #for h in new_Sr_{0}_{1}
           