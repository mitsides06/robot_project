import random as rd

class Grid:
	def __init__(self, size):
		self.size = size
		self.cells = {(row, col) : [] for row in range(size) for col in range(size)}
	
	def generate_random_corner_position(self):
		row = rd.choice([0, self.size-1])
		col = rd.choice([0, self.size-1])
		return (row, col)
	
	def add_drink(self, drink, cell_position):
		try:
			self.cells[cell_position].append(drink)
		except KeyError:
			print(f"Warning: Can't add drink to {cell_position} because the position is out of bounds. Drink not added")
	
	