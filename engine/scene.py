import engine.entity
import engine.components
import engine.file

class Scene:
	def __init__(self, jsonFile, externalComponents=None):
		self._entities = {}

		if jsonFile!= None:
			self.initScene(jsonFile, externalComponents)
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

	def initScene(self, jsonFile, externalComponents=None):
		data = engine.file.getJsonData(jsonFile)

		if "prefabs" in data:
			for prefab in data["prefabs"]:
				if prefab.startswith("#"):
					continue
				file = data["prefabs"][prefab]["file"]
				map = None
				if "map" in data["prefabs"][prefab]:
					map = data["prefabs"][prefab]["map"]
					if map == "none":
						map =None

				self.loadPrefab(file, map, externalComponents)

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
			entity.addComponent(component)

		self.addEntity(entityName, entity)
		return entity

	def __overrideEntityTransform(self, entity, transformList):
		cmp = entity.getComponent("TransformComponent")

		if cmp != None:
			cmp.position = engine.math.Vector(transformList[0], transformList[1])
			if len(transformList) == 4:
				cmp.scale = engine.math.Vector(transformList[2], transformList[3])

	def loadPrefab(self, jsonPath, transformOverrides=None, externalComponents=None):
		data = engine.file.getJsonData(jsonPath)

		if transformOverrides == None:
			for entityName in data["entities"]:
				entityData = data["entities"][entityName]
				entity = self.loadPrefabEntity(entityName, entityData, externalComponents)

		elif isinstance(transformOverrides, list):
			for t in transformOverrides:
				for entityName in data["entities"]:
					entityData = data["entities"][entityName]
					entity = self.loadPrefabEntity(entityName, entityData, externalComponents)

					self.__overrideEntityTransform(entity, t)

		elif isinstance(transformOverrides, dict):
			mapData = engine.file.getTextData(transformOverrides["file"])
			gridSize = [32,32]
			if "gridSize" in transformOverrides:
				gridSize = transformOverrides["gridSize"]
			gridScale =[32,32]
			if "gridScale" in transformOverrides:
				gridScale = transformOverrides["gridScale"]
			relations = {}
			if "relations" in transformOverrides:
				relations = transformOverrides["relations"]

			for y, line in enumerate(mapData.split("\n")):
				for x, char in enumerate(line):
					if not char in relations:
						continue
					entityName = relations[char]
					entityData = data["entities"][entityName]
					entity = self.loadPrefabEntity(entityName, entityData, externalComponents)

					pos = [gridSize[0]*x, gridSize[1]*y]
					t = pos + gridScale

					self.__overrideEntityTransform(entity, t)




	################################

	def addEntity(self, name, entity):
		finalName = name
		sufix = 0
		while finalName in self._entities:
			sufix += 1
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