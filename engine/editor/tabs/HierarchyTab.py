import tkinter

from engine.editor.tab import Tab
import engine.app

class HierarchyTab(Tab):
	def __init__(self, frame):
		super().__init__(frame, "Hierarchy")

		self._listBox = tkinter.Listbox(self._frame)
		self._listBox.pack(side="left", expand=1, fill="both")

		self._scroll = tkinter.Scrollbar(self._frame)
		self._scroll.config(command=self._listBox.yview)
		self._listBox.config(yscrollcommand=self._scroll.set)
		self._scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)


	def update(self):
		self.onModify()

		active = self._listBox.get(tkinter.ACTIVE)
		engine.app.getApp().getEditor().setActiveEntity(active)

	def onModify(self):
		app = engine.app.getApp()
		currentList = self._listBox.get(0, tkinter.END)
		entityList = app.getActiveScene().getEntityList()

		for n, entity in enumerate(currentList):
			if not entity in entityList:
				self._listBox.delete(n)

		for entity in entityList:
			if not entity in currentList:
				self._listBox.insert(tkinter.END, entity)