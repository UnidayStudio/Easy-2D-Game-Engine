import pygame
import pygame_gui

import engine.app

from engine.math import Vector
import engine.math

from engine.gui.uielement import UIElement

class Button(UIElement):
	def __init__(self, buttonName, canvas):
		super().__init__()
		self._name = buttonName
		self._canvas = canvas
		self._element = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (100, 100)),
													 text=self._name,
													 manager=self._canvas.getPygameGuiManager())

		self._functionCallbacks = []

	def loadJsonData(self, jsonData):
		super().loadJsonData(jsonData)

		if "callback" in jsonData:
			callbacks = engine.getApp().getButtonCallbacks()
			if hasattr(callbacks, jsonData["callback"]):
				f = getattr(callbacks, jsonData["callback"])
				self.addFunctionCallback(f)

	def addFunctionCallback(self, function):
		assert(callable(function)), "Error: Function Callbacks must be callable."
		self._functionCallbacks.append(function)

	def _updateFunctionCallbacks(self):
		"""When the user press a button, every function callback attached to
		it is called and recieves the corresponding instance of this button
		class as argument."""
		if self._element.check_pressed():
			for function in self._functionCallbacks:
				function(self)

	def update(self):
		self.updateResolution()
		self._updateFunctionCallbacks()


