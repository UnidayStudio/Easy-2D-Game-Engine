import engine.components

import engine.app

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

	def parseJsonComponents(self, jsonDict):
		externalComponents = engine.app.getApp().getExternalComponents()

		for componentName in jsonDict:
			componentAttr = None

			if hasattr(engine.components, componentName):
				componentAttr = getattr(engine.components, componentName)

			elif externalComponents:
				componentAttr = getattr(externalComponents, componentName)

			if not componentAttr:
				print("Component Not found:", componentName)
				continue

			component = componentAttr()
			component.parseJsonData(jsonDict[componentName])
			self.addComponent(component)

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

	def getComponentList(self):
		return list(self._components.keys())