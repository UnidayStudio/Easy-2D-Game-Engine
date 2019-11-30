import engine


class TestComponent(engine.Component):
	def update(self):
		transform = self.getEntity().getComponent("TransformComponent")
		events = engine.getApp().getEvents()

		if events.pressedKey("K_w"):
			print("in!")
		#if events.activeKey("K_w"):
		#	print("active!")
		if events.releasedKey("K_w"):
			print("out!")