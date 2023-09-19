import random as rd

class Robot:
	def __init__(self, id_, name, position, direction, grid_size):
		self.id = id_
		self.name = name
		self.position = position
		self.direction = direction
		self.grid_size = grid_size
		self.target_position = (rd.choice([0, grid_size-1]), rd.choice([0, grid_size-1]))
	
	def generate_direction_string(self):
		if self.is_north():
			return 'North'
		elif self.is_south():
			return 'South'
		elif self.is_west():
			return 'West'
		else:
			return 'East'

	def greet(self):
		print(f'Hello! My name is {self.name}. My ID is {self.id}.')

	def salut(self):
		print(f'I am currently at {self.target_position}!')
		print('I am finally here enjoying my drink!')
	
	def report(self):
		print(f'I am currenlty at {self.position}, facing {self.generate_direction_string()}.')

	def is_north(self):
		return self.direction == 'n'
	
	def is_south(self):
		return self.direction == 's'
	
	def is_west(self):
		return self.direction == 'w'
	
	def is_east(self):
		return self.direction == 'e'

	def on_boundary(self):
		if self.is_north():
			return self.position[0] <= 0
		elif self.is_south():
			return self.position[0] >= self.grid_size - 1
		elif self.is_east():
			return self.position[1] >= self.grid_size - 1
		else:
			return self.position[1] <= 0
	def on_boundary_statement(self):
		if self.on_boundary():
			print('There is a wall in front of me so I am rotating 90 degrees clockwise!')

	def change_direction(self):
		if self.is_north():
			self.direction = 'e'
		elif self.is_south():
			self.direction = 'w'
		elif self.is_east():
			self.direction = 's'
		else:
			self.direction = 'n'

	def move(self):
		if self.is_north():
			self.position = (self.position[0] - 1, self.position[1])
		elif self.is_south():
			self.position = (self.position[0] + 1, self.position[1])
		elif self.is_east():
			self.position = (self.position[0], self.position[1] + 1)
		else:
			self.position = (self.position[0], self.position[1] - 1)
			
	def move_statement(self):
		print('Moving forward')





k = Robot(3, 'Alex', (3,2), 'w', 9)




	

	