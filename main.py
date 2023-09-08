name = input('What is the name of the robot? ')
first_identifier = 1000
grid_size = 10

row = int(input('What is its current row coordinate? '))
if row < 0:
	row = 0
elif row > grid_size - 1:
	row = grid_size - 1

col = int(input('What is its current column coordinate? '))

init_direction = input('What is its initial direction [n|s|e|w]? ')

if col > grid_size - 1:
	col = grid_size - 1
elif col < 0:
	col = 0

print(f'Hello! My name is {name}! My ID is {first_identifier}!')

if row < 5:
	vertical_axis = 'top'
else:
	vertical_axis = 'bottom'
if col < 5:
	horizontal_axis = 'left'
else:
	horizontal_axis = 'right'

print(f'My current location is {(row,col)}. I am in the {vertical_axis} {horizontal_axis} quadrant.')

current_location = (row,col)
if init_direction == 'n':
	print('I am facing North.')
	print('Moving one step forward.')
	if row != 0:
		row -= 1
		current_location = (row,col)
		if row < 5:
			vertical_axis = 'top'
		else:
			vertical_axis = 'bottom'		
		print(f'My current location is {current_location}. I am in the {vertical_axis} {horizontal_axis} quadrant.')
	else:
		print(f'My current location is {current_location}. I am in the {vertical_axis} {horizontal_axis} quadrant.')

elif init_direction == 's':
	print('I am facing South.')
	print('Moving one step forward.')
	if row != 9:
		row += 1
		current_location = (row,col)
		if row < 5:
			vertical_axis = 'top'
		else:
			vertical_axis = 'bottom'		
		print(f'My current location is {current_location}. I am in the {vertical_axis} {horizontal_axis} quadrant.')
	else:
		print(f'My current location is {current_location}. I am in the {vertical_axis} {horizontal_axis} quadrant.')

elif init_direction == 'e':
	print('I am facing East.')
	print('Moving one step forward.')
	if col != 9:
		col += 1
		current_location = (row,col)
		if col < 5:
			horizontal_axis = 'left'
		else:
			horizontal_axis = 'right'		
		print(f'My current location is {current_location}. I am in the {vertical_axis} {horizontal_axis} quadrant.')
	else:
		print(f'My current location is {current_location}. I am in the {vertical_axis} {horizontal_axis} quadrant.')

else:
	print('I am facing West.')
	print('Moving one step forward.')	
	if col != 0:
		col -= 1
		current_location = (row,col)
		if col < 5:
			horizontal_axis = 'left'
		else:
			horizontal_axis = 'right'		
		print(f'My current location is {current_location}. I am in the {vertical_axis} {horizontal_axis} quadrant.')
	else:
		print(f'My current location is {current_location}. I am in the {vertical_axis} {horizontal_axis} quadrant.')


