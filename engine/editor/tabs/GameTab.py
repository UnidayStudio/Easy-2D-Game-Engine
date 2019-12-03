import os

from engine.editor.tab import Tab

class GameTab(Tab):
	def __init__(self, frame):
		super().__init__(frame, "Game")

		os.environ['SDL_WINDOWID'] = str(self._frame.winfo_id())
		os.environ['SDL_VIDEODRIVER'] = 'windib'