import pygame
import pygame_gui

import engine.app
import engine.file

from engine.gui.button import *

class Canvas():
	def __init__(self):
		theme = engine.file.getPath("data/gui.json")
		self._manager = pygame_gui.UIManager((640, 480), theme)
		self._buttons = {}

	def getPygameGuiManager(self):
		return self._manager

	def getButton(self, buttonName):
		if not buttonName in self._buttons:
			self._buttons[buttonName] = Button(buttonName, self)
		return self._buttons[buttonName]

	def removeButton(self, buttonName):
		if buttonName in self._buttons:
			self._buttons[buttonName].kill()
			del self._buttons[buttonName]

	def _cleanupKilledButtons(self):
		toRemove = []
		for buttonName in self._buttons:
			if self._buttons[buttonName].isKilled():
				toRemove.append(buttonName)
		for buttonName in toRemove:
			del self._buttons[buttonName]


	def _processEvents(self):
		app = engine.app.getApp()
		events = app.getEvents().getPygameEvents()

		for event in events:
			self._manager.process_events(event)

	def _updateButtons(self):
		for button in self._buttons:
			self._buttons[button].update()

	def update(self):
		app = engine.app.getApp()
		display = app.getRenderer().getDisplay()

		self._cleanupKilledButtons()
		self._processEvents()

		self._manager.update(app.getDeltaTime())
		self._manager.draw_ui(display)

		self._updateButtons()
