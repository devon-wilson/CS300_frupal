# Name Jesse Coyle
# Date 1/18/2020
# File tile.py
# Desc definitions for tiles

class Terrain:
	def __init__(self, id, name, ascii, energy):
		# Note(Jesse): member integer that identifies this specific Obstacle
		#              0 _cannot be valid_
		self.id = id # Research(Jesse): We might not need the id
		self.name = name # Note(Jesse): In case we want to tell the user
		self.ascii = ascii # Note(Jesse): The singular ascii character that will be represented on the map
		self.energy = energy # Note(Jesse): Energy spent on navigating tile

class Obstacle:
	def __init__(self, id, name, ascii, energy):
		# Note(Jesse): member integer that identifies this specific Obstacle
		#              0 _can be valid_ in the event there is no obstacle on the tile
		self.id = id # Research(Jesse): We might not need the id
		self.name = name # Note(Jesse): For use in the store... in case we want to mention what tool goes to what obstacle?
		self.ascii = ascii # Note(Jesse): The singular ascii character that will be represented on the map
		self.energy = energy # Note(Jesse): Energy spent on removing obstacle

class Tiles:
	terrain = []
	obstacles = []

	def addTerrain(self, name, ascii, energy):
		id = len(self.terrain) + 1
		terrain = Terrain(id, name, ascii, energy)
		self.terrain.append(terrain)

	def addObstacle(self, name, ascii, energy):
		id = len(self.obstacles) + 1
		obstacle = Obstacle(id, name, ascii, energy)
		self.obstacles.append(obstacle)
