import pygame

import engine.renderer
from engine.timer import Timer

class __App:
	def __init__(self):
		pygame.init()
		self._deltaTimer = Timer()
		self._deltaTime = 0

		self._activeScene = None
		self._renderer = engine.renderer.Renderer()
	################################

	def run(self):
		while pygame.event.poll().type != pygame.QUIT:
			self._deltaTimer.reset()
			scene = self.getActiveScene()

			self._renderer.fill([20,20,20])

			if scene:
				scene.updateLogic()
				scene.updatePhysics()
				scene.draw()

			pygame.display.flip()
			self._deltaTime = self._deltaTimer.get()

	def getRenderer(self):
		return self._renderer

	def getDeltaTime(self):
		return self._deltaTime

	################################

	def setActiveScene(self, scene):
		self._activeScene = scene

	def getActiveScene(self):
		return self._activeScene

__app = __App()

def getApp():
	return __app