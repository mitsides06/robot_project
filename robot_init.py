import random as rd
from robot import Robot






def load_names_from_file(filename):
	names = []
	textfile = open(filename)
	for line in textfile:
		name = line.strip()
		names.append(name)
	return names




def setup_robot(grid_size):
	""" Initialise the robot name, ID, and initial position and direction.
	
	Args:
		grid_size (int): The size of the grid.
	
	Returns:
		str : Robot name
		int : Robot ID
		int : Robot's row coordinate
		int : Robot's column coordinate
		str : Robot's direction ("n", "s", "e", or "w")
	"""		
	names = load_names_from_file('robot_names.txt')
	name = rd.choice(names)
	id = rd.randint(0,10000000000000000)
	row = rd.randint(0,grid_size - 1)
	col = rd.randint(0,grid_size - 1)
	position = (row, col)
	direction = rd.choice(('n', 's', 'e', 'w'))
	return Robot(id, name, position, direction, grid_size)
