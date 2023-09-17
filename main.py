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



def navigate(Robot):
	""" Navigate robot.

	It prints out its current location and where it is facing. Then it prints out its next movement. It returns None if it is at the required location optherwise it returns the new row and col position and the new direction in a tuple.

	Args:
		str : Robot's direction ("n", "s", "e", or "w")
		int : Robot's row coordinate
		int : Robot's col coordinate
		int : Robot's target row
		int : Robot's target col
		int : Grid size
	
	Returns:
		int : Robot's new row coordinate
		int : Robot's new col coordinate
		str : Robot's new direction
	"""

	if Robot.position == Robot.target_position:
		Robot.salut()
		return None
	else:
		Robot.report()
		if Robot.on_boundary():
			Robot.on_boundary_statement()
			Robot.change_direction()
			return Robot
		else:
			Robot.move_statement()
			Robot.move()
			return Robot
			












		
			





def run_simulation(grid_size=10):
	""" Start robot navigation simulation.
		
	Args:
		grid_size (int): The size of the grid. Default to 10.
		target_row (int): The target row coordinate. Defaults to 9.
		target_col (int): The target column coordinate. Defaults to 9.
	"""
	final_dic = {}
	id_list = []
	for i in range(3):
		Robot = setup_robot(grid_size)
		id_list.append(Robot.id)
		final_dic[Robot.id] = Robot
		Robot.greet()
	print()
	for i in range(3):
		print(f"{final_dic[id_list[i]].name} is searching for its drink!")
		ans = navigate(final_dic[id_list[i]])
		while ans is not None:
			final_dic[id_list[i]] = ans
			ans = navigate(final_dic[id_list[i]])
		print()
	
	return None
	

grid_size = 10
run_simulation(grid_size=grid_size)