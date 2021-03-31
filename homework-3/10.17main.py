# Ezequiel Zapata PSID: 001863257

# part 1 creating a class for items to purchase by item name, price, and quantity
class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):
        print(self.item_name + " " + str(self.item_quantity) + " @ $" + str(self.item_price) + " = $" +
              str(self.item_price * self.item_quantity))

# part 2 prompt the user for 2 items and have the program output the total cost of both items together


if __name__ == '__main__':
    print("Item 1")
    item1 = ItemToPurchase()
    item1.item_name = input('Enter the item name:\n')
    item1.item_price = int(input('Enter the item price:\n'))
    item1.item_quantity = int(input('Enter the item quantity:\n'))

    print("\nItem 2")
    item2 = ItemToPurchase()
    item2.item_name = input('Enter the item name:\n')
    item2.item_price = int(input('Enter the item price:\n'))
    item2.item_quantity = int(input('Enter the item quantity:\n'))

    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()

    total = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)

    print("\nTotal: $" + str(total))