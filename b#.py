# B#

import sys

# open file
src = open( sys.argv[1], "r" )
lines = "".join( x for x in src )
lines = lines.split("\n")

# points
points = {}

# define a point
def defPoint( name, rawDef ):
	definition = "".join( tok for tok in rawDef )
	coords = definition.split(";")
	for i in range(len(coords)):
		coords[i] = int( coords[i] )
	points[name] = coords

for line in lines:
	tokens = line.split(" ")
	if tokens[1] == "->":
		name = tokens[0]
		objType = tokens[2]
		if objType == "Point":
			defPoint( name, tokens[3:] )