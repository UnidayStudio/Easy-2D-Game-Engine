class Entity:
	def __init__(self):
		self._components = {}

	################################

	def spawn(self):
		"""This Method is called when the object is added to the scene"""
		for component in self._components:
			self._components[component].spawn()

	def update(self):
		for component in self._components:
			self._components[component].update()

	def draw(self):
		for component in self._components:
			self._components[component].draw()

	################################

	def addComponent(self, component):
		name = component.__class__.__name__
		assert(not name in self._components),"An object can't have two components of the same type."

		self._components[name] = component
		self._components[name].setEntity(self)

	def getComponent(self, name : str):
		if not name in self._components:
			return None
		return self._components[name]

	def removeComponent(self, name : str):
		del self._components[name]