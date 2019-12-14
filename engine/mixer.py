import pygame

import engine.file

class Mixer():
	def __init__(self):
		self._sounds = {}

	def _getSound(self, name):
		if not name in self._sounds:
			try:
				img = pygame.mixer.Sound(engine.file.getPath(name))
			except:
				return None
			self._sounds[name] = img
		return self._sounds[name]

	def playSound(self, name):
		sound = self._getSound(name)
		if sound == None:
			return
		sound.play()
