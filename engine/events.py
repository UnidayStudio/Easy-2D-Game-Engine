import pygame

KEY_UP 		= pygame.KEYUP
KEY_PRESS 	= 1337
KEY_DOWN 	= pygame.KEYDOWN

MOUSE_UP 	= pygame.MOUSEBUTTONUP
MOUSE_PRESS = 1337
MOUSE_DOWN 	= pygame.MOUSEBUTTONDOWN

LEFT_MOUSE 			= 1
MOUSE_WHEEL 		= 2
RIGHT_MOUSE 		= 3
MOUSE_WHEEL_UP 		= 4
MOUSE_WHEEL_DOWN 	= 5


class Events():
	def __init__(self):
		self._keyboardEvents = {}
		self._mouseEvents = {}
		self._quit = False

	def getQuit(self):
		return self._quit

	################################

	def pressedKey(self, key):
		key = self._getPygameKey(key)
		if key in self._keyboardEvents:
			if self._keyboardEvents[key] == KEY_DOWN:
				return True
		return False

	def activeKey(self, key):
		key = self._getPygameKey(key)
		return key in self._keyboardEvents

	def releasedKey(self, key):
		key = self._getPygameKey(key)
		if key in self._keyboardEvents:
			if self._keyboardEvents[key] == KEY_UP:
				return True
		return False

	################################

	def pressedMouse(self, button):
		if button in self._mouseEvents:
			if self._mouseEvents[button] == MOUSE_DOWN:
				return True
		return False

	def activeMouse(self, button):
		return button in self._mouseEvents

	def releasedMouse(self, button):
		if button in self._mouseEvents:
			if self._mouseEvents[button] == MOUSE_UP:
				return True
		return False

	################################

	def _getPygameKey(self, value):
		if not isinstance(value, str):
			return value
		return getattr(pygame, value)

	def updateEvents(self):
		# Keyboard...
		toRemove = []
		for event in self._keyboardEvents:
			if self._keyboardEvents[event] == KEY_DOWN:
				self._keyboardEvents[event] = KEY_PRESS
			if self._keyboardEvents[event] == KEY_UP:
				toRemove.append(event)
		for obj in toRemove:
			del self._keyboardEvents[obj]

		# Mouse...
		toRemove = []
		for event in self._mouseEvents:
			if self._mouseEvents[event] == MOUSE_DOWN:
				self._mouseEvents[event] = MOUSE_PRESS
			if self._mouseEvents[event] == MOUSE_UP:
				toRemove.append(event)
		for obj in toRemove:
			del self._mouseEvents[obj]

		# Updating the dictionaries again
		for event in pygame.event.get():
			eventType = event.type

			if eventType == pygame.QUIT:
				self._quit = True

			elif eventType in [KEY_UP, KEY_DOWN]:
				eventKey = event.key
				self._keyboardEvents[eventKey] = eventType

			elif eventType in [MOUSE_UP, MOUSE_DOWN]:
				eventButton = event.button
				self._mouseEvents[eventButton] = eventType