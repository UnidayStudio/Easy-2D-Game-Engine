import engine

class RigidBodyComponent(engine.Component):
	def solveCollision(self, other):
		a = self.getEntity().getComponent("TransformComponent")
		b = other.getEntity().getComponent("TransformComponent")

		assert (a != None and b != None)

		centerA = a.getCenterPosition()
		centerB = b.getCenterPosition()

		endA = a.getEndPosition()
		endB = b.getEndPosition()

		x, y = 0, 0
		if centerA.x < centerB.x:	x = b.position.x - endA.x
		else:						x = endB.x - a.position.x

		if centerA.y < centerB.y:	y = b.position.y - endA.y
		else:						y = endB.y - a.position.y

		if abs(x) < abs(y):	a.position.x += x
		else:				a.position.y += y

	def applyGravity(self, x, y):
		transform = self.getEntity().getComponent("TransformComponent")
		transform.position.x += x
		transform.position.y += y