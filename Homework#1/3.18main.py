# Ezequiel Zapata PSID: 001863257

# part 1 to prompt to input a wall's height and width and calculate the wall's area.

wall_height = input('Enter wall height (feet):\n')
wall_width = input('Enter wall width (feet):\n')

print('Wall area: {:d} square feet'.format(int(wall_width) * int(wall_height)))

# part 2 adding the amount of paint needed to paint the wall as a floating point output.

gallons_needed = float((int(wall_width) * int(wall_height)) / 350)
print('Paint needed: {:.2f} gallons'.format(gallons_needed))

# part 3 adding the amount of 1 gallon cans needed to paint the wall. Using a math function.

import math
cans_needed = math.ceil(gallons_needed)
print('Cans needed: {} can(s)'.format(cans_needed))

# part 4 adding an input to the user to choose which color of paint they want to use (red, blue, green) and how much
# that color of paint costs.

paint_colors = {'red': 35, 'blue': 25, 'green': 23}  # this is a dictionary for the paint colors with their prices.
color = input('\nChoose a color to paint the wall:\n')
print('Cost of purchasing '+ color +' paint: $'+ str(cans_needed * paint_colors[color]))
