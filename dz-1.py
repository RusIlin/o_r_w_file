with open('recipes.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    for dish in file:
        count = int(file.readline().strip())
        temp_list = []
        for i in range(count):
            ingredient_name, quantity, measure = file.readline().split('|')
            temp_list.append(
                {'ingredient_name': ingredient_name.strip(), 'quantity': quantity.strip(), 'measure': measure.strip()}
            )
        cook_book[dish.strip()] = temp_list
        file.readline()

print(cook_book)
