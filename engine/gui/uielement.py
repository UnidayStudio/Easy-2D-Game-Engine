import pygame
import pygame_gui

import engine.app

from engine.math import Vector
import engine.math

class UIElement():
	def __init__(self):
		self._element = None

		self._lastResolution = [-1, -1]
		self._position = Vector(0.4, 0.45)
		self._scale = Vector(0.2, 0.1)

		self._killed = False

	def isKilled(self):
		return self._killed

	def kill(self):
		if not self._element:
			return
		self._element.kill()
		self._killed = True

	def setPosition(self, x, y):
		self._position.x = engine.math.clamp(x, 0.0, 1.0)
		self._position.y = engine.math.clamp(y, 0.0, 1.0)
		self.updateResolution(True)

	def setScale(self, x, y):
		self._scale.x = engine.math.clamp(x, 0.01, 1.0)
		self._scale.y = engine.math.clamp(y, 0.01, 1.0)
		self.updateResolution(True)

	def updateResolution(self, force=False):
		if not self._element:
			return
		renderer = engine.app.getApp().getRenderer()
		res = renderer.getResolution()
		if res == self._lastResolution and not force:
			return
		self._lastResolution = res

		res= Vector(res[0], res[1])

		position = res * self._position
		scale = res * self._scale

		self._updateElementTransform(position.getList(), scale.getList())

	def _updateElementTransform(self, position, scale):
		self._element.set_position(position)
		self._element.set_dimensions(scale)

	############################

	def loadJsonData(self, jsonData):
		if "position" in jsonData:
			pos = jsonData["position"]
			self.setPosition(pos[0], pos[1])
		if "scale" in jsonData:
			scale = jsonData["scale"]
			self.setScale(scale[0], scale[1])

	def update(self):
		self.updateResolution()
