import os, sys

def getPath(file):
	APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))
	return  os.path.join(APP_FOLDER, file)