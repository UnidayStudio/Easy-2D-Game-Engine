import pygame
import pygame_gui

import engine.app

from engine.math import Vector
import engine.math

class Button():
	def __init__(self, buttonName, canvas):
		self._name = buttonName
		self._canvas = canvas
		self._button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (100, 100)),
													text=self._name,
													manager=self._canvas.getPygameGuiManager())

		self._lastResolution = [-1,-1]
		self._position = Vector(0.4,0.45)
		self._scale = Vector(0.2, 0.1)

		self._functionCallbacks = []
		self._killed = False

	def loadJsonData(self, jsonData):
		if "position" in jsonData:
			pos = jsonData["position"]
			self.setPosition(pos[0], pos[1])
		if "scale" in jsonData:
			scale = jsonData["scale"]
			self.setScale(scale[0], scale[1])

	def isKilled(self):
		return self._killed

	def addFunctionCallback(self, function):
		assert(callable(function)), "Error: Function Callbacks must be callable."
		self._functionCallbacks.append(function)

	def setPosition(self, x, y):
		self._position.x = engine.math.clamp(x, 0.0, 1.0)
		self._position.y = engine.math.clamp(y, 0.0, 1.0)
		self._updateResolution(True)

	def setScale(self, x, y):
		self._scale.x = engine.math.clamp(x, 0.01, 1.0)
		self._scale.y = engine.math.clamp(y, 0.01, 1.0)
		self._updateResolution(True)

	def _updateResolution(self, force=False):
		renderer = engine.app.getApp().getRenderer()
		res = renderer.getResolution()
		if res == self._lastResolution and not force:
			return
		self._lastResolution = res

		res= Vector(res[0], res[1])

		position = res * self._position
		scale = res * self._scale

		self._button.set_position(position.getList())
		self._button.set_dimensions(scale.getList())

	def _updateFunctionCallbacks(self):
		"""When the user press a button, every function callback attached to
		it is called and recieves the corresponding instance of this button
		class as argument."""
		if self._button.check_pressed():
			for function in self._functionCallbacks:
				function(self)

	def update(self):
		self._updateResolution()
		self._updateFunctionCallbacks()

	def kill(self):
		self._button.kill()
		self._killed = True
