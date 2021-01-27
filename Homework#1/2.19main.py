# part 1 to prompt the user for the number of cups of lemon juice, water, and agave nectar to make lemonade.

num_lemon_cups = float(input('Enter amount of lemon juice (in cups):\n'))
num_water_cups = float(input('Enter amount of water (in cups):\n'))
num_nectar_cups = float(input('Enter amount of agave nectar (in cups):\n'))
num_servings = float(input('How many servings does this make?\n'))

print('\nLemonade ingredients - yields {:.2f} servings'.format(num_servings))
print('{:.2f} cup(s) lemon juice'.format(num_lemon_cups))
print('{:.2f} cup(s) water'.format(num_water_cups))
print('{:.2f} cup(s) agave nectar'.format(num_nectar_cups))

# part 2 to prompt the user to specify the desired number of servings.

num_servings_required = float(input('\nHow many servings would you like to make?\n'))

print('\nLemonade ingredients - yields {:.2f} servings'.format(num_servings_required))
print('{:.2f} cup(s) lemon juice'.format(num_lemon_cups * num_servings_required / num_servings))
print('{:.2f} cup(s) water'.format(num_water_cups * num_servings_required / num_servings))
print('{:.2f} cup(s) agave nectar'.format(num_nectar_cups * num_servings_required / num_servings))

# part 3 converting the ingredient measurements from part 2 to gallons.

print('\nLemonade ingredients - yields {:.2f} servings'.format(num_servings_required))
print('{:.2f} gallon(s) lemon juice'.format(num_lemon_cups * num_servings_required / num_servings / 16))
print('{:.2f} gallon(s) water'.format(num_water_cups * num_servings_required / num_servings / 16))
print('{:.2f} gallon(s) agave nectar'.format(num_nectar_cups * num_servings_required / num_servings / 16))
