import engine

class RectComponent(engine.Component):

	def __init__(self):
		super().__init__()

		self.color = [255,255,255]

	def draw(self):
		renderer = engine.getApp().getRenderer()
		transform = self.getEntity().getComponent("TransformComponent")

		renderer.drawRect(self.color, transform)
