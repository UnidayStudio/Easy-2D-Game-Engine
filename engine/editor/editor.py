import tkinter
from tkinter import ttk
import os

from engine.editor.frame import Frame
import engine.app

class Editor():
	def __init__(self, horizontal=True):
		self._root = tkinter.Tk()
		self._panedRoot = Frame(self._root, horizontal, True)

		self._frames = []

		self._activeEntity = None

		self._initEditor()

	def _initEditor(self):
		self._root.protocol("WM_DELETE_WINDOW", self.onClose)
		self._root.state("zoomed")
		self._root.title("Ez2D Game Engine - Editor")

		frame0 = self.newFrame(False)
		gameTab = frame0.newTab("GameTab")


		frame1 = frame0.newFrame(False)
		script = frame1.newTab("ScriptTab")
		test1 = frame1.newTab()

		frame2 = self.newFrame(False)
		test2 = frame2.newTab("HierarchyTab")

		frame3 = frame2.newFrame(False)
		entity = frame3.newTab("EntityTab")

		#frame3 = frame2.newFrame(False)
		#test3 = frame3.newTab()

	def getActiveEntity(self):
		if self._activeEntity == None:
			return None
		scene = engine.app.getApp().getActiveScene()
		object = scene.getEntity(self._activeEntity)
		return object

	def getActiveEntityName(self):
		return self._activeEntity

	def setActiveEntity(self, entityName):
		self._activeEntity = entityName

	def newFrame(self, horizontal=True):
		frame = self._panedRoot.newFrame(horizontal)
		self._frames.append(frame)
		return frame

	def update(self):
		self._root.update()

		for frame in self._frames:
			frame.update()

	def onClose(self):
		engine.app.getApp().getEvents().quitGame()
		print("Engine Editor Closed!")
