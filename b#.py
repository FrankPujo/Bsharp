# B#

import sys
import json

# open file
src = open( sys.argv[1], "r" )
lines = "".join( x for x in src )
lines = lines.split("\n")

# entities
points = {}
rects = {}

# exportable entities
expPoints = {}
expRects = {}

# useful variables
lastValue = 0

# define a point
class Point:
	def __init__( self, name, rawDef ):
		# define
		definition = "".join( tok for tok in rawDef )
		coords = definition.split(";")
		self.name = name
		self.x = int(coords[0])
		self.y = int(coords[1])
		# exportable
		expPoints[self.name] = { "x": self.x, "y": self.y }

# define a line (also "rect(s)" to disambiguate from script's lines)
class Rect:
	def __init__( self, name, rawDef ):
		# define
		definition = "".join( tok for tok in rawDef )
		params = definition.split("x")
		self.name = name
		self.m = int(params[0])
		self.q = int(params[1])
		# exportable
		expRects[self.name] = { "m": self.m, "q": self.q }

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
		# definitions
		name = tokens[0]
		objType = tokens[2]
		if objType == "Point":
			# define point
			points[name] = Point( name, tokens[3:] )
		elif objType == "Rect" or objType == "Line":
			# define line
			rects[name] = Rect( name, tokens[3:] )
	elif tokens[0] == "?":
		# conditions
		if tokens[2] == "[":
			# point on line
			lastValue = checkPointBelongRect( tokens[1], tokens[3] )

# export
if len( sys.argv ) > 2:
	if sys.argv[2] == "EXP":
		data = {
			"points": expPoints,
			"rects": expRects
		}
		origFile = sys.argv[1]
		file = open( origFile[:-3] + "json" , "w" )
		json_data = json.dump( data, file )
# test some stuff
#print( lastValue )