import engine


class TestComponent(engine.Component):
	def __init__(self):
		super().__init__()

		self.test = False
		self.description = "Player"

	def update(self):
		transform = self.getEntity().getComponent("TransformComponent")
		events = engine.getApp().getEvents()

		if events.pressedKey("K_w"):
			print("in!")
		#if events.activeKey("K_w"):
		#	print("active!")
		if events.releasedKey("K_w"):
			print("out!")