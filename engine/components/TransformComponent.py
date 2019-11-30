import engine

class TransformComponent(engine.Component):
	def __init__(self):
		super().__init__()

		self.position = engine.math.Vector(0,0)
		self.scale = engine.math.Vector(100, 100)

	def getEndPosition(self):
		return self.position + self.scale

	def getCenterPosition(self):
		return self.position + (self.scale / 2.0)