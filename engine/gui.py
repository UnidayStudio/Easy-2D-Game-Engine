import pygame
import pygame_gui

import engine.app

class Gui():
	def __init__(self):
		self._manager = pygame_gui.UIManager((640, 480))

		button1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 230), (150, 40)),
									 text='Button 01',
									 manager=self._manager)
		button2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 180), (150, 40)),
											   text='Another Button',
											   manager=self._manager)

	def draw(self):
		app = engine.app.getApp()
		display = app.getRenderer().getDisplay()

		self._manager.update(app.getDeltaTime())
		self._manager.draw_ui(display)
