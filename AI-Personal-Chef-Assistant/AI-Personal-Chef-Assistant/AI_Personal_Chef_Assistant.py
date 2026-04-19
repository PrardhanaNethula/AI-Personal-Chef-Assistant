diet = input("Enter your diet (veg/non-veg): ")
budget = int(input("Enter your weekly budget: "))

if diet == "veg":
    meals = ["Rice + Dal", "Vegetable Curry", "Paneer Dish"]
else:
    meals = ["Chicken Curry", "Egg Bhurji", "Fish Fry"]

print("\nYour Meal Plan:")
for meal in meals:
    print("-", meal)
