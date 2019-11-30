import pygame

class EventSystem():
	def __init__(self):
		self._events = {}
		self._quit = False

	def getQuit(self):
		return self._quit

	def updateEvents(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self._quit = True
				continue

			
