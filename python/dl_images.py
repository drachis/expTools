# -*- coding: utf-8 -*-
"""
Created on Thu Nov 06 17:16:02 2014

@author: toli
"""

#http://promo.na.leagueoflegends.com/sru-map-assets/6/47/39.png
import urllib2
import cStringIO
from PIL import Image

def downloadImages():
    files = {}
    for h in range(0,47):
        for v in range(0,40):
            filename = ("C:/Riot Games/new_Sr_{0}_{1}.png".format(h,v))
            files[filename] = (cStringIO.StringIO(urllib2.urlopen("http://promo.na.leagueoflegends.com/sru-map-assets/6/{0}/{1}.png".format(h,v)).read()))
        print h
    for filename in files:
        image_info = Image.open(files[filename])
        image_info.save(filename)
        files[filename].close()

def compositeImage(h = horizontal, v = Vertical, files):
    files[]
    image = Image.image.new("RGB", (h,v) ,"Black")
    
 
if __name__ == "__main__":
    #downloadIMages()

    for h in new_Sr_{0}_{1}
           