import pygame

class Timer():
	def __init__(self):
		self._time = 0
		self.reset()

	def _getTicks(self): # in seconds
		return pygame.time.get_ticks() / 1000

	def set(self, value):
		self._time = self._getTicks() - value

	def reset(self):
		self.set(0)

	def get(self):
		return self._getTicks() - self._time