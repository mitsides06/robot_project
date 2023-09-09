import random as rd

name = input('What is the name of the robot? ')
first_identifier = 1000
grid_size = 10

row = rd.randint(0,9)
col = rd.randint(0,9)
init_direction = rd.choice(('n', 's', 'e', 'w'))

#row = int(input('What is its current row coordinate? '))
#if row < 0:
#	row = 0
#elif row > grid_size - 1:
#	row = grid_size - 1

#col = int(input('What is its current column coordinate? '))

#init_direction = input('What is its initial direction [n|s|e|w]? ')

#if col > grid_size - 1:
#	col = grid_size - 1
#elif col < 0:
#	col = 0



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
	while row > 0:                                # checking if it has space to move forward
		print('Moving one step forward.')
		row -= 1
		current_location = (row,col)
		if row < 5:                         # checking if it changed quadrant
			vertical_axis = 'top'
		else:
			vertical_axis = 'bottom'		
		print(f'My current location is {current_location}. I am in the {vertical_axis} {horizontal_axis} quadrant.')
	else:
		print('I have a wall in front of me!')
		

elif init_direction == 's':
	print('I am facing South.')
	while row < 9:                                  # checking if it has space to move forawrd
		print('Moving one step forward.')
		row += 1
		current_location = (row,col)
		if row < 5:                            # checking if it changed quadrant
			vertical_axis = 'top'
		else:
			vertical_axis = 'bottom'		
		print(f'My current location is {current_location}. I am in the {vertical_axis} {horizontal_axis} quadrant.')
	else:
		print('I have a wall in front of me!')
		

elif init_direction == 'e':
	print('I am facing East.')
	while col < 9:                                # checking if it has space to move forward
		print('Moving one step forward.')
		col += 1
		current_location = (row,col)
		if col < 5:                         # checking ig it changed quadrant
			horizontal_axis = 'left'
		else:
			horizontal_axis = 'right'		
		print(f'My current location is {current_location}. I am in the {vertical_axis} {horizontal_axis} quadrant.')
	else:
		print('I have a wall in front of me!')
		
else:
	print('I am facing West.')	
	while col > 0:                                           # checking it has space to move forward
		print('Moving one step forward.')
		col -= 1
		current_location = (row,col)
		if col < 5:                                      # checking if it changed quadrant
			horizontal_axis = 'left'
		else:
			horizontal_axis = 'right'		
		print(f'My current location is {current_location}. I am in the {vertical_axis} {horizontal_axis} quadrant.')
	else:
		print('I have a wall in front of me!')
		

