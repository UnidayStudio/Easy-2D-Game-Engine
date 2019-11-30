import engine

class ColliderComponent(engine.Component):
	def dettectCollision(self, other):
		a = self.getEntity().getComponent("TransformComponent")
		b = other.getEntity().getComponent("TransformComponent")
		assert(a != None and b != None)

		endA = a.getEndPosition()
		endB = b.getEndPosition()

		if a.position.x < endB.x and endA.x > b.position.x:
			if a.position.y < endB.y and endA.y > b.position.y:
				return True
		return False