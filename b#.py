# B#

import sys

# open file
src = open( sys.argv[1], "r" )
lines = "".join( x for x in src )
lines = lines.split("\n")

# entities
points = {}
rects = {}

# useful variables
lastValue = 0

# define a point
class Point:
	def __init__( self, name, rawDef ):
		definition = "".join( tok for tok in rawDef )
		coords = definition.split(";")
		self.name = name
		self.x = int(coords[0])
		self.y = int(coords[1])

# define a line (also "rect(s)" to disambiguate from script's lines)
class Rect:
	def __init__( self, name, rawDef ):
		definition = "".join( tok for tok in rawDef )
		params = definition.split("x")
		self.name = name
		self.m = int(params[0])
		self.q = int(params[1])

# check if a point belongs to a rect
def checkPointBelongRect( point, rect ):
	rectM = rects.get( rect ).m
	rectQ = rects.get( rect ).q
	pX = points.get( point ).x
	pY = points.get( point ).y
	return int(pY) == int(pX) * int(rectM) + int(rectQ)

# read file line by line - Main loop -
for line in lines:
	tokens = line.split(" ")
	if tokens[1] == "->":
		name = tokens[0]
		objType = tokens[2]
		if objType == "Point":
			points[name] = Point( name, tokens[3:] )
		elif objType == "Rect" or objType == "Line":
			rects[name] = Rect( name, tokens[3:] )
	elif tokens[0] == "?":
		if tokens[2] == "[":
			lastValue = checkPointBelongRect( tokens[1], tokens[3] )

# test some stuff
print( lastValue )