import engine

def exampleButton(button):
	print("Button Pressed!")
	scene = engine.getActiveScene()
	scene.setActiveGuiCanvas("canvas2")