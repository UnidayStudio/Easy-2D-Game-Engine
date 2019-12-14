import os, sys


def getPath(file):
	#APP_FOLDER = os.path.dirname(os.path.abspath(__file__))
	APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))
	out = os.path.join(APP_FOLDER, file)
	return out

def getJsonData(jsonPath):
	file = open(getPath(jsonPath), "r")
	data = eval(file.read())
	file.close()
	return data

def getTextData(textPath):
	file = open(getPath(textPath), "r")
	data = file.read()
	file.close()
	return data