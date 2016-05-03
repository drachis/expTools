""" 
	rename the latest file to auto0.g for printing on bukito bot
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

