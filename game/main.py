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