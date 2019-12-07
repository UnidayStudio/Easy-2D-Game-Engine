import engine.entity
import engine.components
import engine.file

class Scene:
	def __init__(self):
		self._entities = {}

	################################

	def updateLogic(self):
		for entity in self._entities:
			self._entities[entity].update()

	def updatePhysics(self):
		id = list(self._entities.keys())
		numEntities = len(id)

		for x in range(numEntities):
			rigidBody = self._entities[id[x]].getComponent("RigidBodyComponent")
			if rigidBody == None:
				continue

			rigidBody.applyGravity(0, 1)

			for y in range(x+1, numEntities):
				collider = self._entities[id[y]].getComponent("ColliderComponent")
				if collider != None:
					if collider.dettectCollision(rigidBody):
						rigidBody.solveCollision(collider)

	def draw(self):
		for entity in self._entities:
			self._entities[entity].draw()

	def getEntityList(self):
		return list(self._entities.keys())

	################################

	def loadPrefabEntity(self, entityName, entityDict, externalComponents=None):
		entity = engine.entity.Entity()

		for componentName in entityDict["components"]:
			componentAttr = None

			if hasattr(engine.components, componentName):
				componentAttr = getattr(engine.components, componentName)
			# print("Default Component: ", componentName)

			elif externalComponents:
				componentAttr = getattr(externalComponents, componentName)
			# print("External Component: ", componentName)

			if not componentAttr:
				# print("Component Not found:", componentName)
				continue

			component = componentAttr()

			componentData = entityDict["components"][componentName]
			for attrName in componentData:
				stack = attrName.split(".")
				endStack = component
				if len(stack) > 1:
					for n in range(len(stack) - 1):
						endStack = getattr(endStack, stack[n])

				setattr(endStack, stack[-1], componentData[attrName])
			# print("\tAttr: ", attrName, " = ", componentData[attrName])

			entity.addComponent(component)

		self.addEntity(entityName, entity)

	def loadPrefab(self, jsonPath, externalComponents=None):
		file = open(engine.file.getPath(jsonPath), "r")
		data = eval(file.read())

		for entityName in data["entities"]:
			self.loadPrefabEntity(entityName, data["entities"][entityName], externalComponents)


	################################

	def addEntity(self, name, entity):
		finalName = name
		sufix = 1
		while finalName in self._entities:
			finalName = name+" ("+str(sufix)+")"

		self._entities[finalName] = entity
		self._entities[finalName].spawn()

		return finalName

	def removeEntity(self, name):
		assert(name in self._entities),"Entity not Found!"
		del self._entities[name]

	def getEntity(self, name):
		return self._entities[name]

	def getAllEntities(self, prefix):
		out = []
		for entity in self._entities:
			if entity.startswith(prefix):
				out.append(self._entities[entity])
		return out

	def removeAllEntities(self, prefix):
		for entity in self._entities:
			if entity.startswith(prefix):
				del self._entities[entity]