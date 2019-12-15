from engine.math.Vector import *


def lerp(value, target, average):
	return value + ((target - value) * average)

def clamp(value, toMin, toMax):
	return max(toMin, min(value, toMax))

def map(value, fromMin, fromMax, toMin, toMax):
	v = clamp(value, fromMin, fromMax)
	v -= fromMin
	v /= (fromMax - fromMin)
	return lerp(toMin, toMax, v)
