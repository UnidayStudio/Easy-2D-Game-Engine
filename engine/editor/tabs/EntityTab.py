import os
import tkinter

from engine.editor.tab import Tab
import engine.app


class EntityTab(Tab):
	def __init__(self, frame):
		super().__init__(frame, "Entity")

		#self._scroll = tkinter.Scrollbar(self._frame)
		#self._scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)

		self._frameData = tkinter.Canvas(self._frame, scrollregion=(0,0,1000,1000))
		#self._frameData.config(yscrollcommand=self._scroll.set)
		#self._scroll.config(command=self._frameData.yview)
		self._frameData.pack(side=tkinter.LEFT,expand=1, fill="both")

		self._currentEntity = None
		self._entity = None

		self._components = {}

	def update(self):
		active = engine.app.getApp().getEditor().getActiveEntityName()

		if active != self._currentEntity:
			self._currentEntity = active
			self._entity = engine.app.getApp().getActiveScene().getEntity(self._currentEntity)
			self.onModify()

		if self._entity != None:
			self.updateEntityVariables()

	def _updateClass(self, classObj, data):
		for key in data:
			if isinstance(data[key], dict):
				self._updateClass(getattr(classObj, key), data[key])
			else:
				try:
					keyData = type(getattr(classObj, key))(data[key].get())
					setattr(classObj, key, keyData)
				except: pass

	def updateEntityVariables(self):
		for component in self._components:
			cmpData = self._components[component]
			cmp = self._entity.getComponent(component)
			self._updateClass(cmp, cmpData)

	def _interfaceClass(self, name, classObj, customFrame=None):
		#TODO: This method smells bad, needs refactoring
		frame = self._frameData
		if customFrame != None:
			frame = customFrame

		group = tkinter.LabelFrame(frame, text=name)
		group.pack(expand=0, fill="x")

		vars = classObj.__dir__()

		data = {}
		for attName in vars:
			if not attName.startswith("_"):
				attr = getattr(classObj, attName)
				if callable(attr):
					continue

				subFrame = tkinter.Frame(group)
				subFrame.pack(expand=1, fill="x")

				widget = None
				if isinstance(attr, bool):
					data[attName] = tkinter.IntVar()
					data[attName].set(int(attr))
					widget = tkinter.Checkbutton(subFrame, variable=data[attName])
				elif isinstance(attr, str):
					#data[attName] = tkinter.StringVar()
					#data[attName].set(attr)
					widget = tkinter.Entry(subFrame)
					widget.delete(0, "end")
					widget.insert(0, attr)
				elif isinstance(attr, int):
					#data[attName] = tkinter.IntVar()
					#data[attName].set(attr)
					widget = tkinter.Spinbox(subFrame)
					widget.delete(0, "end")
					widget.insert(0, attr)
				elif isinstance(attr, float):
					#data[attName] = tkinter.DoubleVar()
					#data[attName].set(attr)
					widget = tkinter.Spinbox(subFrame)
					#widget.setvar(value=str(attr))
					widget.delete(0, "end")
					widget.insert(0, attr)
				else:
					data[attName] = self._interfaceClass(attName, attr, subFrame)

				if widget != None:
					if not isinstance(attr, bool):
						data[attName] = widget
					label= tkinter.Label(subFrame, text=attName)
					#label.grid(row=0, column=0)
					#widget.grid(row=0, column=1)
					label.pack(side="left",expand=0, fill="x")
					widget.pack(side="right",expand=0, fill="x")

		return data

	def _interfaceComponent(self, component):
		cmpName = component.__class__.__name__
		self._components[cmpName] = self._interfaceClass(cmpName, component)

	def onModify(self):
		for widget in self._frameData.winfo_children():
			widget.destroy()

		components = self._entity.getComponentList()

		self._components = {}
		for component in components:
			self._interfaceComponent(self._entity.getComponent(component) )
