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

	scene = engine.Scene()

	scene.loadPrefab("data/prefabs/gameplay.json", game.data.components)

	app.setActiveScene(scene)

	app.run()



if __name__ == "__main__":
	main()