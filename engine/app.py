import pygame

import engine.renderer
from engine.timer import Timer
from engine.events import Events
from engine.gui import Gui

from engine.editor import Editor

class __App:
	def __init__(self, withEditor=True):
		self._editor = None
		self._withEditor = withEditor
		if self._withEditor:
			self._editor = Editor()

		pygame.init()

		self._deltaTimer = Timer()
		self._deltaTime = 0

		self._activeScene = None
		self._renderer = engine.renderer.Renderer()

		self.events = Events()

		self.gui = Gui()
	################################

	def getRenderer(self):
		return self._renderer

	def getDeltaTime(self):
		return self._deltaTime

	def getEvents(self):
		return self.events

	def getEditor(self):
		return self._editor

	################################

	def setActiveScene(self, scene):
		self._activeScene = scene

	def getActiveScene(self):
		return self._activeScene

	################################

	def run(self):
		gameloop = True
		while gameloop: #pygame.event.poll().type != pygame.QUIT:
			self._deltaTimer.reset()
			self.events.updateEvents()

			if self.events.getQuit():
				gameloop = False

			scene = self.getActiveScene()

			self._renderer.fill([20,20,20])

			if scene:
				scene.updateLogic()
				scene.updatePhysics()
				scene.draw()

			self.gui.draw()

			self._renderer.update()
			if self._withEditor:
				self._editor.update()

			self._deltaTime = self._deltaTimer.get()


__app = __App()

def getApp():
	return __app