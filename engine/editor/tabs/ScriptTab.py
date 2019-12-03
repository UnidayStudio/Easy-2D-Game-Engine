import tkinter
import keyword

from engine.editor.tab import Tab

class ScriptTab(Tab):
	def __init__(self, frame):
		super().__init__(frame, "Script")

		self._text = tkinter.Text(self._frame, font=("Helvetica", 12))
		self._text.pack(side="left", expand=1, fill="both")

		self._scroll = tkinter.Scrollbar(self._frame)
		self._scroll.config(command=self._text.yview)
		self._text.config(yscrollcommand=self._scroll.set)
		self._scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)

		#self._entry = tkinter.Entry(self._frame, )

		self._text.bind("<<Modified>>", self._onModify)

	def updateTextHighlights(self):
		text = self._text.get("1.0", tkinter.END)

		data = text.split("\n")
		reservedWords = keyword.kwlist + ["self", "print"]

		for tag in self._text.tag_names():
			self._text.tag_delete(tag)

		for lineNumber, line in enumerate(data):
			word = ""
			lineIndex = str(lineNumber+1)

			for charNumber, char in enumerate(line):
				startPos = lineIndex + "." + str(charNumber - len(word))
				endPos = lineIndex + "." + str(charNumber)
				tag = word + "-" + startPos + "-" + endPos

				if char == "#":
					endPos = lineIndex + "." + str(len(line))
					self._text.tag_add(tag, startPos, endPos)
					self._text.tag_config(tag, foreground="red")
					break

				if char in [" ", "\t", "(", ")"]:
					if word in reservedWords:
						self._text.tag_add(tag, startPos, endPos)
						self._text.tag_config(tag, foreground="blue", font=("Helvetica", 12, "bold"))
					word = ""
				elif char in ["\"","'"] and word != "":
					if char == word[0]:
						endPos = lineIndex + "." + str(charNumber+1)
						self._text.tag_add(tag, startPos, endPos)
						self._text.tag_config(tag, foreground="green")
						word = ""
					else:
						word =char
				else:
					word += char


	def _onModify(self, value=None):
		flag = self._text.edit_modified()

		if flag:
			self.updateTextHighlights()

		self._text.edit_modified(False)

	#for tag in keyword.kwlist:
		#	self._text.tag_add(tag, "1.0", "1.8")
		#	self._text.tag_config(tag, background="black",foreground="blue")

