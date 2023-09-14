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
	row = rd.randint(0,grid_size)
	col = rd.randint(0,grid_size)
	position = (row, col)
	direction = rd.choice(('n', 's', 'e', 'w'))
	return Robot(id, name, position, direction)

def print_robot_greeting(Robot):
	print(f"Hello. My name is {Robot.name}. My ID is {Robot.id}.")

def navigate(Robot,
             target_position,
             grid_size):
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

	if Robot.position == target_position:
		print(f"I am currently at {target_position}!")
		print('I am finally here enjoying my drink!')
		return None
	else:
		if Robot.direction == "n":
			print(f"I am currenlty at {Robot.position}, facing North.")
			if Robot.position[0] <= 0:
				print('There is a wall in front of me so I am rotating 90 degrees clockwise!')
				Robot.direction = 'e'
				return Robot
			else:
				Robot.position = (Robot.position[0] - 1, Robot.position[1])
				print('Moving forward')
				return Robot

		elif Robot.direction == "s":
			print(f"I am currenlty at {Robot.position}, facing South.")
			if Robot.position[0] >= grid_size - 1:
				print('There is a wall in front of me so I am rotating 90 degrees clockwise!')
				Robot.direction = 'w'
				return Robot
			else:
				Robot.position = (Robot.position[0] + 1, Robot.position[1])
				print('Moving forward')
				return Robot

		elif Robot.direction == "e":
			print(f"I am currenlty at {Robot.position}, facing East.")
			if Robot.position[1] >= grid_size - 1:
				print('There is a wall in front of me so I am rotating 90 degrees clockwise!')
				Robot.direction = 's'
				return Robot
			else:
				Robot.position = (Robot.position[0], Robot.position[1] + 1)
				print('Moving forward')
				return Robot

		else:
			print(f"I am currenlty at {Robot.position}, facing West.")
			if Robot.position[1] <= 0:
				print('There is a wall in front of me so I am rotating 90 degrees clockwise!')
				Robot.direction = 'n'
				return Robot
			else:
				Robot.position = (Robot.position[0], Robot.position[1] - 1)
				print('Moving forward')
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
		print_robot_greeting(Robot)
	print()
	for i in range(3):
		target_list = [0,grid_size - 1]
		target_position = (rd.choice(target_list), rd.choice(target_list))
		print(f"{final_dic[id_list[i]].name} is searching for its drink!")
		ans = navigate(final_dic[id_list[i]], target_position, grid_size)
		while ans is not None:
			final_dic[id_list[i]] = ans
			ans = navigate(final_dic[id_list[i]], target_position, grid_size)
		print()
	
	return None
	

grid_size = 10
run_simulation(grid_size=grid_size)