
class Component:
	def __init__(self):
		self._entity = None

	################################

	def spawn(self):
		pass

	def update(self):
		pass

	def draw(self):
		pass

	################################

	def getEntity(self):
		return self._entity

	def setEntity(self, entity):
		self._entity = entity
