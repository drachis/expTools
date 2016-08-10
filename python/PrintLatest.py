""" 
	marlin firmware auto0.g copy file
	rename the latest file in the current directory to auto0.g 
	for printing 3d printing, saves a bit of time.
"""
import os
import glob
import shutil

if __name__ == "__main__":
	newest = max(glob.iglob('*.*'), key=os.path.getctime)
	_dir = os.path.dirname(os.path.realpath(__file__))
	auto0g = os.path.join(_dir, "auto0.g")
	if os.path.exists(auto0g):
		os.remove(auto0g)
	shutil.copy(newest,auto0g )
	print(newest)

