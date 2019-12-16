import pygame
import pygame_gui

import engine.app
import engine.file

from engine.gui.button import *
from engine.gui.textbox import *
from engine.gui.healthbar import *

class Canvas():
	def __init__(self):
		theme = engine.file.getPath("data/gui.json")
		self._manager = pygame_gui.UIManager((640, 480), theme)
		self._elements = {}

	def loadJsonData(self, jsonData):
		if "buttons" in jsonData:
			for buttonName in jsonData["buttons"]:
				button = self.addButton(buttonName)
				button.loadJsonData(jsonData["buttons"][buttonName])

		if "textBoxes" in jsonData:
			for textBoxName in jsonData["textBoxes"]:
				textBox = self.addTextBox(textBoxName)
				textBox.loadJsonData(jsonData["textBoxes"][textBoxName])

		if "healthBars" in jsonData:
			for healthBarName in jsonData["healthBars"]:
				healthBar = self.addHealthBar(healthBarName)
				healthBar.loadJsonData(jsonData["healthBars"][healthBarName])

	def getPygameGuiManager(self):
		return self._manager

	################################

	def addButton(self, buttonName):
		if not buttonName in self._elements:
			self._elements[buttonName] = Button(buttonName, self)
		return self._elements[buttonName]

	def addTextBox(self, textBoxName, htmlText=""):
		if not textBoxName in self._elements:
			self._elements[textBoxName] = TextBox(htmlText, self)
		return self._elements[textBoxName]

	def addHealthBar(self, healthBarName):
		if not healthBarName in self._elements:
			self._elements[healthBarName] = HealthBar(self)
		return self._elements[healthBarName]

	################################

	def getElement(self, elementName):
		if not elementName in self._elements:
			return None#self._elements[elementName] = Button(elementName, self)
		return self._elements[elementName]

	################################

	def removeElement(self, elementName):
		if elementName in self._elements:
			self._elements[elementName].kill()
			del self._elements[elementName]

	def _cleanupKilledElements(self):
		toRemove = []
		for elementName in self._elements:
			if self._elements[elementName].isKilled():
				toRemove.append(elementName)
		for elementName in toRemove:
			del self._elements[elementName]


	def _processEvents(self):
		app = engine.app.getApp()
		events = app.getEvents().getPygameEvents()

		for event in events:
			self._manager.process_events(event)

	def _updateElements(self):
		for elementName in self._elements:
			self._elements[elementName].update()

	def update(self):
		app = engine.app.getApp()
		display = app.getRenderer().getDisplay()

		self._cleanupKilledElements()
		self._processEvents()

		self._manager.update(app.getDeltaTime())
		self._manager.draw_ui(display)

		self._updateElements()
