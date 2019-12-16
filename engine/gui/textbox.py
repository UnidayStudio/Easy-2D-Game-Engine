import pygame
import pygame_gui

import engine.app

from engine.math import Vector
import engine.math

from engine.gui.uielement import UIElement

class TextBox(UIElement):
	def __init__(self, htmlText, canvas):
		super().__init__()
		self._htmlText = htmlText
		self._canvas = canvas
		self.__createUITextBox()


	def __createUITextBox(self):
		if self._element != None:
			self._element.kill()
		self._element = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((0, 0), (100, 100)),
													html_text=self._htmlText,
													manager=self._canvas.getPygameGuiManager())

	def updateHtmlText(self, htmlText):
		self._htmlText = htmlText
		self.__createUITextBox()
		self.updateResolution(True)

	def loadJsonData(self, jsonData):
		super().loadJsonData(jsonData)

		if "html" in jsonData:
			self.updateHtmlText(jsonData["html"])

	def update(self):
		super().update()
