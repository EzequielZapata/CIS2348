# Ezequiel Zapata PSID: 001863257

# part 1 Creating a class so that the constructor can be called with a food name and give grams of fat, carbs, and protein.
class FoodItem:  # TODO: Define constructor with parameters to initialize instance # attributes (name, fat, carbs, protein)

    def __init__(self, name="None", fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


if __name__ == "__main__":

    food_itemA = FoodItem()

    item_name = input()
    amount_fat = float(input())
    amount_carbs = float(input())
    amount_protein = float(input())

    food_itemB = FoodItem(item_name, amount_fat, amount_carbs, amount_protein)

    num_servings = float(input())

    food_itemA.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings, food_itemA.get_calories(num_servings)))

    print()

    food_itemB.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings, food_itemB.get_calories(num_servings)))