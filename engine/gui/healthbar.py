import pygame
import pygame_gui

from engine.gui.uielement import UIElement

class HealthBar(UIElement):
	def __init__(self, canvas):
		super().__init__()
		self._canvas = canvas

		class HealthData():
			def __init__(self):
				self.health_capacity = 150
				self.current_health = 27
		self._healthData = HealthData()
		self._element = pygame_gui.elements.UIScreenSpaceHealthBar(relative_rect=pygame.Rect((10, 10), (200, 30)),
													   	sprite_to_monitor= self._healthData,
														manager=self._canvas.getPygameGuiManager())

		self._healthData.current_health = 80

	def setCurrentHealth(self, currentHealth : float):
		self._healthData.current_health = currentHealth

	def setMaxHealth(self, maxHealth : float):
		self._healthData.health_capacity = maxHealth

	def _updateElementTransform(self, position, scale):
		self._element.kill()
		self._element = pygame_gui.elements.UIScreenSpaceHealthBar(relative_rect=pygame.Rect(position, scale),
																   sprite_to_monitor=self._healthData,
																   manager=self._canvas.getPygameGuiManager())
		#

	def loadJsonData(self, jsonData):
		super().loadJsonData(jsonData)

		if "currentHealth" in jsonData:
			self.setCurrentHealth(jsonData["currentHealth"])
		if "maxHealth" in jsonData:
			self.setMaxHealth(jsonData["maxHealth"])

	def update(self):
		super().update()