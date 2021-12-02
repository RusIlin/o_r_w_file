from pprint import pprint

with open('recipes.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    for dish in file:
        dish_name = dish.strip()
        count = int(file.readline())
        temp_list = []
        for i in range(count):
            ingredient_name, quantity, measure = file.readline().split('|')
            temp_list.append(
                {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure.strip()}
            )
        cook_book[dish_name] = temp_list
        file.readline()
    pprint(cook_book)