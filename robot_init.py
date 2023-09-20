import random as rd
from robot import Robot
from grid import Grid

class RobotInitialiser:
	def __init__(self, names, quantity, grid):
		self.directions = ["s", "n", "w", "e"]
		self.names = names
		self.grid= grid
		self.quantity = quantity
	
	def _generate_name(self):
		return rd.choice(self.names)
	
	def _generate_id(self):
		return rd. randint(0,100000)
	
	def _generate_position(self):
		row = rd.randint(0, self.grid.size - 1)
		col = rd.randint(0, self.grid.size - 1)
		position = (row, col)
		return position
	
	def _generate_direction(self):
		return rd.choice(self.directions)
	
	def create_robots(self):
		robot_dic = {}
		for i in range(self.quantity):
			id_ = self._generate_id()
			name = self._generate_name()
			position = self._generate_position()
			direction = self._generate_direction()
			robot_dic[id_] = Robot(id_, name, position, direction, self.grid)
		return robot_dic
			









