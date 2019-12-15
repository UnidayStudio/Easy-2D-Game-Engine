import pygame

import engine.renderer
import engine.file
import engine.gui

from engine.timer import Timer
from engine.events import Events
from engine.scene import Scene
from engine.mixer import Mixer

from engine.editor import Editor

class __App:
	def __init__(self, withEditor=False):
		self._editor = None
		self._withEditor = withEditor
		if self._withEditor:
			self._editor = Editor()

		pygame.init()

		self._deltaTimer = Timer()
		self._deltaTime = 0

		self._activeScene = None

		self._renderer = engine.renderer.Renderer()
		self._mixer = Mixer()
		self.events = Events()

		self._buttonCallbacks = None

	################################

	def initGame(self, mainFile, externalComponents=None, buttonCallbacks=None):
		self._buttonCallbacks = buttonCallbacks
		data = engine.file.getJsonData(mainFile)

		if "game" in data:
			if "title" in data["game"]:
				pygame.display.set_caption(data["game"]["title"])
			if "icon" in data["game"]:
				img = self.getRenderer().getImage(data["game"]["icon"])
				pygame.display.set_icon(img)

		if "mainScene" in data:
			scene = Scene(data["mainScene"], externalComponents)
			self.setActiveScene(scene)

	def getRenderer(self):
		return self._renderer

	def getMixer(self):
		return self._mixer

	def getDeltaTime(self):
		return self._deltaTime

	def getEvents(self):
		return self.events

	def getEditor(self):
		return self._editor

	###

	def getButtonCallbacks(self):
		return self._buttonCallbacks

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
				scene.drawGui()

			self._renderer.update()
			if self._withEditor:
				self._editor.update()

			self._deltaTime = self._deltaTimer.get()


__app = __App()

def getApp():
	return __app

###################################

def getRenderer():
	return getApp().getRenderer()

def getEvents():
	return getApp().getEvents()

def getMixer():
	return getApp().getMixer()

def getDeltaTime():
	return getApp().getDeltaTime()

def getActiveScene():
	return getApp().getActiveScene()