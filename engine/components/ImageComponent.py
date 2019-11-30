import engine

class ImageComponent(engine.Component):

	def __init__(self):
		super().__init__()

		self.image = ""

	def draw(self):
		renderer = engine.getApp().getRenderer()
		transform = self.getEntity().getComponent("TransformComponent")

		renderer.drawImage(self.image, transform)
