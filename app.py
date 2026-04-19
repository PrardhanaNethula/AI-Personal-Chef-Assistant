diet = input("Enter your diet (veg/non-veg): ")
budget = int(input("Enter your weekly budget: "))

if diet == "veg":
    meals = ["Rice + Dal", "Vegetable Curry", "Paneer Dish", "Palak Dish"]
else:
    meals = ["Chicken Curry", "Egg Bhurji", "Fish Fry", "Egg Fried Rice"]

print("\nYour Meal Plan:")
for meal in meals:
    print("-", meal)
