import random as rd

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
	return (name, id, position, direction)

def print_robot_greeting(name, identifier):
	print(f'Hello. My name is {name}. My ID is {identifier}.')

def navigate(current_direction,
    	     position,
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

	if position == target_position:
		print(f'I am currently at {target_position}!')
		print('I am finally here enjoying my drink!')
		return None
	else:
		if current_direction == "n":
			print(f'I am currenlty at {position}, facing North.')
			if position[0] == 0:
				print('There is a wall in front of me so I am rotating 90 degrees clockwise!')
				return (position, 'e')
			else:
				position = (position[0] - 1, position[1])
				print('Moving forward')
				return (position, current_direction)

		elif current_direction == "s":
			print(f'I am currenlty at {position}, facing South.')
			if position[0] == grid_size - 1:
				print('There is a wall in front of me so I am rotating 90 degrees clockwise!')
				return (position, 'w')
			else:
				position = (position[0] + 1, position[1])
				print('Moving forward')
				return (position, current_direction)

		elif current_direction == "e":
			print(f'I am currenlty at {position}, facing East.')
			if position[1] == grid_size - 1:
				print('There is a wall in front of me so I am rotating 90 degrees clockwise!')
				return (position, 's')
			else:
				position = (position[0], position[1] + 1)
				print('Moving forward')
				return (position, current_direction)

		else:
			print(f'I am currenlty at {position}, facing West.')
			if position[1] == 0:
				print('There is a wall in front of me so I am rotating 90 degrees clockwise!')
				return (position, 'n')
			else:
				position = (position[0], position[1] - 1)
				print('Moving forward')
				return (position, current_direction)
		
			





def run_simulation(grid_size=10):
	""" Start robot navigation simulation.
		
	Args:
		grid_size (int): The size of the grid. Default to 10.
		target_row (int): The target row coordinate. Defaults to 9.
		target_col (int): The target column coordinate. Defaults to 9.
	"""
	l = []
	for i in range(3):
		l.append(setup_robot(grid_size))
		print_robot_greeting(l[i][0], l[i][1])
	print()
	for i in range(3):
		target_list = [0,grid_size - 1]
		target_position = (rd.choice(target_list), rd.choice(target_list))
		print(f'{l[i][0]} is searching for its drink!')
		ans = navigate(l[i][3], l[i][2], target_position, grid_size)
		while ans is not None:
			position, direction = ans
			ans = navigate(direction, position, target_position, grid_size)
		print()
	
	return None
	

grid_size = 10
run_simulation(grid_size=grid_size)