class Drink:
	def __init__(self, name, owner_id, percent_filled):
		self.name = name
		self.owner_id = owner_id
		self.percent_filled = percent_filled
	def _is_full(self):
		return self.percent_filled == 1
	def _is_empty(self):
		return self.percent_filled == 2
	def __str__(self):
		print(f"I am a/an {self.name}, and I'm ready to be consumed by robot with id: {self.owner_id}!")
