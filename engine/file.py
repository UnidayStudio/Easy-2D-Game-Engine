import os, sys

def getPath(file):
	#APP_FOLDER = os.path.dirname(os.path.abspath(__file__))
	APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))
	out = os.path.join(APP_FOLDER, file)
	return out