import tkinter
from tkinter import ttk

class Tab():
	def __init__(self, frame, title="Tab"):
		self._frame = ttk.Frame(frame.getFrame(), width=500, height=500)
		frame.getFrame().add(self._frame, text=title)

	def update(self):
		pass