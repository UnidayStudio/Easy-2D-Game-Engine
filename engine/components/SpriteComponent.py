import pygame

import engine

from engine.math.Vector import Vector
from engine.timer import Timer
import engine.app

class SpriteComponent(engine.Component):
	def __init__(self):
		super().__init__()
		self._timer = Timer()

		self.image = ""
		self.grid = Vector(1,1)
		self.frameStart = 0
		self.frameEnd = 10
		self.currentFrame = 0
		self.framesPerSecond = 0

	def _getTimeBetweenFrames(self):
		if self.framesPerSecond == 0:
			return -1
		return 1.0 / self.framesPerSecond

	def _nextFrame(self) -> bool:
		time = self._getTimeBetweenFrames()
		if time == -1:
			return False
		if self._timer.get() >= time:
			return True
		return False

	def _goToNextFrame(self):
		self.currentFrame += 1
		if self.currentFrame > self.frameEnd:
			self.currentFrame = self.frameStart
		self._timer.reset()

	def _getFramePositions(self):
		x = int(self.grid.x)
		y = int(self.grid.y)

		column = self.currentFrame // x
		line = (self.currentFrame - (column*x))

		return [column/x, line/y, 1/x, 1/y]

	def _getFrameImage(self):
		renderer = engine.app.getApp().getRenderer()
		image = renderer.getImage(self.image)
		imageSize = image.get_rect().size

		pos = self._getFramePositions()

		pos[0] *= imageSize[0]
		pos[1] *= imageSize[1]
		pos[2] *= imageSize[0]
		pos[3] *= imageSize[1]

		frame = pygame.Surface([pos[2], pos[3]], pygame.SRCALPHA)
		frame.blit(image, (0,0), pos)

		return frame

	def setAnimation(self, frameStart, frameEnd, current=None):
		self.frameStart = frameStart
		self.frameEnd = frameEnd
		if current == None:
			self.currentFrame = self.frameStart
		else:
			self.currentFrame = current

	def draw(self):
		renderer = engine.getApp().getRenderer()
		transform = self.getEntity().getComponent("TransformComponent")

		if self._nextFrame():
			self._goToNextFrame()
			#print("frame: ", self.currentFrame)

		renderer.drawImage(self._getFrameImage(), transform)
