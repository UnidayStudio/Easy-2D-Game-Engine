import sys
import os

dirpath = os.getcwd()
sys.path.append(dirpath)
sys.path.append(dirpath+"\\..\\")

if getattr(sys, "frozen", False):
	os.chdir(sys._MEIPASS)

import engine
import game.data.components

def main():
	app = engine.getApp()
	app.initGame("data/main.json", game.data.components)
	app.run()

if __name__ == "__main__":
	main()