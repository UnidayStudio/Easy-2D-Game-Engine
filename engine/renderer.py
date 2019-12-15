import pygame
import os

import engine.file
from engine.math import Vector

class Renderer():
	def __init__(self):
		self._resolution = [640, 480]
		self._display = pygame.display.set_mode(self._resolution, pygame.RESIZABLE)
		#pygame.display.init()

		self._images = {}

		self._cameraPosition = Vector(0,0)
		self._cameraScale = 350

	################################

	def resize(self, w, h):
		self._resolution =[w, h]
		self._display = pygame.display.set_mode(self._resolution, pygame.RESIZABLE)

	def getResolution(self):
		return self._resolution

	def getCameraPosition(self):
		return self._cameraPosition

	def setCameraPosition(self, vec):
		self._cameraPosition = vec

	def getCameraScale(self):
		return self._cameraScale

	def setCameraScale(self, scale):
		self._cameraScale = scale

	def vecToCameraView(self, vec):
		return vec * (self._resolution[1] / self._cameraScale)

	def transformToCameraData(self, transform):
		pos = transform.position - self._cameraPosition
		#pos.x += (self._resolution[0] - self._cameraScale) / 2
		#pos.y += (self._resolution[1] / 2)
		pos = self.vecToCameraView(pos)
		scale = self.vecToCameraView(transform.scale)
		return pos, scale

	################################

	def fill(self, color):
		self._display.fill(color)

	def drawRect(self, color, transform):
		pos, scale = self.transformToCameraData(transform)
		data = (pos.x, pos.y, scale.x, scale.y)

		pygame.draw.rect(self._display, color, data)

	def drawImage(self, imageName, transform):
		pos, scale = self.transformToCameraData(transform)

		image = None
		if isinstance(imageName, str):
			image = self.getImage(imageName)
		else:
			image = imageName
			#print("wit")
		if image == None:
			return

		outImage = pygame.transform.scale(image, (int(scale.x), int(scale.y)))

		self._display.blit(outImage, (int(pos.x), int(pos.y)))

	def update(self):
		pygame.display.flip()
		#pygame.display.update()

	################################

	def getImage(self, name):
		if not name in self._images:
			try:
				img = pygame.image.load(engine.file.getPath(name))
			except:
				return None
			self._images[name] = img.convert_alpha()
		return self._images[name]

	def getDisplay(self):
		return self._display

