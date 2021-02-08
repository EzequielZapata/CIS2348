# Ezequiel Zapata PSID: 001863257

# part 1 displaying the menu.

print("Davy's auto shop services\n"
      "Oil change -- $35\n"
      "Tire rotation -- $19\n"
      "Car wash -- $7\n"
      "Car wax -- $12\n")

# part 2 prompting the user to choose 2 services from the menu.

print('Select first service:')
service_1 = input()
print('Select second service:')
service_2 = input()

# part 3 outputting an invoice to the user for their selected services, including the individual service costs and total costs.
# part 4 is also added to include '-' as an option if the user doesn't choose a service.

print("\nDavy's auto shop invoice\n")

total = 0

if service_1 == 'Oil change':
    print('Service 1: Oil change, $35')
    total = total + 35
elif service_1 == 'Tire rotation':
    print('Service 1: Tire rotation, $19')
    total = total + 19
elif service_1 == 'Car wash':
    print('Service 1: Car wash, $7')
    total = total + 7
elif service_1 == 'Car wax':
    print('Service 1: Car wax, $12')
    total = total + 12
elif service_1 == '-':
    print('Service 1: No service')
    total = total + 0
else:
    print('Service 1: error')

if service_2 == 'Oil change':
    print('Service 2: Oil change, $35')
    total = total + 35
elif service_2 == 'Tire rotation':
    print('Service 2: Tire rotation, $19')
    total = total + 19
elif service_2 == 'Car wash':
    print('Service 2: Car wash, $7')
    total = total + 7
elif service_2 == 'Car wax':
    print('Service 2: Car wax, $12')
    total = total + 12
elif service_2 == '-':
    print('Service 2: No service')
    total = total + 0
else:
    print('Service 2: error')

print('\nTotal: ${}'.format(total))