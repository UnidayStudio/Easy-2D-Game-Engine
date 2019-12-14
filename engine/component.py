
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

	def parseJsonData(self, jsonData):
		for attrName in jsonData:
			stack = attrName.split(".")
			endStack = self
			if len(stack) > 1:
				for n in range(len(stack) - 1):
					endStack = getattr(endStack, stack[n])

			setattr(endStack, stack[-1], jsonData[attrName])

	def getEntity(self):
		return self._entity

	def setEntity(self, entity):
		self._entity = entity
