import pygame
import os

import engine.file

class Renderer():
	def __init__(self):
		self._display = pygame.display.set_mode([640, 480], pygame.RESIZABLE)
		#pygame.display.init()

		self._images = {}

	################################

	def resize(self, w, h):
		self._display = pygame.display.set_mode([w, h], pygame.RESIZABLE)

	def fill(self, color):
		self._display.fill(color)

	def drawRect(self, color, transform):
		pos = transform.position
		scale = transform.scale
		data = (pos.x, pos.y, scale.x, scale.y)

		pygame.draw.rect(self._display, color, data)

	def drawImage(self, imageName, transform):
		pos = transform.position
		scale = transform.scale

		image = self.getImage(imageName)
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

