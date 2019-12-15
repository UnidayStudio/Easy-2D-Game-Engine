import math

class Vector():
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def copy(self):
		return Vector(self.x, self.y)

	def getCopy(self):
		return self.copy()

	def length(self):
		return math.sqrt(self.x**2 + self.y**2)

	def getLength(self):
		return self.length()

	def normalize(self):
		l = self.length()
		if l != 0:
			self.x /= l
			self.y /= l

	def normalized(self):
		out = self.copy()
		out.normalize()
		return out

	def getList(self):
		return [self.x, self.y]

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

	def __ne__(self, other):
		return self.x != other.x or self.y != other.y

	def __add__(self, other):
		return Vector(self.x + other.x, self.y + other.y)

	def __iadd__(self, other):
		self.x += other.x
		self.y += other.y

	def __sub__(self, other):
		return Vector(self.x - other.x, self.y - other.y)

	def __isub__(self, other):
		self.x -= other.x
		self.y -= other.y

	def __mul__(self, other):
		out = self.copy()
		if isinstance(other, Vector):
			out.x *= other.x
			out.y *= other.y
		else:
			out.x *= other
			out.y *= other
		return out

	def __imul__(self, other):
		if isinstance(other, Vector):
			self.x *= other.x
			self.y *= other.y
		else:
			self.x *= other
			self.y *= other

	def __truediv__(self, other):
		out = self.copy()
		if isinstance(other, Vector):
			out.x /= other.x
			out.y /= other.y
		else:
			out.x /= other
			out.y /= other
		return out

	def __itruediv__(self, other):
		if isinstance(other, Vector):
			self.x /= other.x
			self.y /= other.y
		else:
			self.x /= other
			self.y /= other
