import pygame

import engine.file

class Renderer():
	def __init__(self):
		#| pygame.OPENGLBLIT
		#bArgs = pygame.DOUBLEBUF | pygame.OPENGLBLIT | pygame.RESIZABLE
		#bArgs = pygame.RESIZABLE
		self._display = pygame.display.set_mode([640, 480])

		self._images = {}

	################################

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
		outImage = pygame.transform.scale(image, (int(scale.x), int(scale.y)))

		self._display.blit(outImage, (int(pos.x), int(pos.y)))

	################################

	def getImage(self, name):
		if not name in self._images:
			#f = engine.file.getPath(name)
			self._images[name] = pygame.image.load(name).convert_alpha()
		return self._images[name]

	def getDisplay(self):
		return self._display

