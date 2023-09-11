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
	direction = rd.choice(('n', 's', 'e', 'w'))
	return (name, id, row, col, direction)

def print_robot_greeting(name, identifier):
	print(f'Hello. My name is {name}. My ID is {identifier}.')

def navigate(current_direction,
             current_row,
             current_col,
             target_row,
             target_col,
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

	if current_row == target_row and current_col == target_col:
		print(f'I am currently at {(target_row, target_col)}!')
		print('I am finally here enjoying my drink!')
		return None
	else:
		if current_direction == "n":
			print(f'I am currenlty at {(current_row, current_col)}, facing North.')
			if current_row == 0:
				print('There is a wall in front of me so I am rotating 90 degrees clockwise!')
				return (current_row, current_col, 'e')
			else:
				print('Moving forward')
				return (current_row - 1, current_col, current_direction)

		elif current_direction == "s":
			print(f'I am currenlty at {(current_row, current_col)}, facing South.')
			if current_row == grid_size - 1:
				print('There is a wall in front of me so I am rotating 90 degrees clockwise!')
				return (current_row, current_col, 'w')
			else:
				print('Moving forward')
				return (current_row + 1, current_col, current_direction)

		elif current_direction == "e":
			print(f'I am currenlty at {(current_row, current_col)}, facing East.')
			if current_col == grid_size - 1:
				print('There is a wall in front of me so I am rotating 90 degrees clockwise!')
				return (current_row, current_col, 's')
			else:
				print('Moving forward')
				return (current_row, current_col + 1, current_direction)

		else:
			print(f'I am currenlty at {(current_row, current_col)}, facing West.')
			if current_col == 0:
				print('There is a wall in front of me so I am rotating 90 degrees clockwise!')
				return (current_row, current_col, 'n')
			else:
				print('Moving forward')
				return (current_row, current_col - 1, current_direction)
		
			





def run_simulation(grid_size=10, target_row=9, target_col=9):
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
		target_row, target_col = rd.choice(target_list), rd.choice(target_list)
		print(f'{l[i][0]} is searching for its drink!')
		ans = navigate(l[i][4], l[i][2], l[i][3], target_row, target_col, grid_size)
		while ans is not None:
			row, col, direction = ans
			ans = navigate(direction, row, col, target_row, target_col, grid_size)
		print()
	
	return None
	

grid_size = 10
run_simulation(grid_size=grid_size)