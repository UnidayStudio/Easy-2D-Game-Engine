import tkinter
from tkinter import ttk

from engine.editor.tab import Tab
import engine.editor.tabs

class Frame():
	def __init__(self, panedRoot, horizontal=True, baseFrame=False):
		orientation = tkinter.VERTICAL
		if horizontal:	orientation = tkinter.HORIZONTAL

		self._paned = tkinter.PanedWindow(panedRoot, orient=orientation)

		self._baseFrame = baseFrame
		self._frame = None

		if not self._baseFrame:
			self._frame = ttk.Notebook(self._paned)
			self._paned.add(self._frame)

			panedRoot.add(self._paned)
		else:
			self._paned.pack(expand=1, fill="both")

		self._tabs = []
		self._childs = []

	def update(self):
		for tab in self._tabs:
			tab.update()
		for child in self._childs:
			child.update()

	def getPaned(self):
		return self._paned

	def getFrame(self):
		return self._frame

	def newTab(self, tabName=None):
		if self._baseFrame:
			return None
		tabAttr = Tab
		if tabName != None:
			tabAttr = getattr(engine.editor.tabs, tabName)
		tab = tabAttr(self)
		self._tabs.append(tab)
		return tab

	def newFrame(self, horizontal=True):
		childFrame = Frame(self.getPaned(), horizontal)
		self._childs.append(childFrame)
		return childFrame