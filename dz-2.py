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


def get_shop_list_by_dishes(dishes, person_count):
    order = {}
    for dish in dishes:
        for result in cook_book[dish]:
            if result['ingredient_name'] in order.keys():
                order[result['ingredient_name']]['quantity'] += int(result['quantity'])
            else:
                order[result['ingredient_name']] = {}
                order[result['ingredient_name']]['measure'] = result['measure']
                order[result['ingredient_name']]['quantity'] = int(result['quantity']) * person_count
    return order


pprint(get_shop_list_by_dishes(['Омлет', 'Омлет'], 2))
