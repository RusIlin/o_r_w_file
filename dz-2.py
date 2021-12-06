from pprint import pprint


def dict_collector(file_path):
    with open(file_path, 'r', encoding='utf-8') as file_work:
        menu = {}
        for line in file_work:
            dish_name = line[:-1]
            counter = file_work.readline().strip()
            list_of_ingredient = []
            for i in range(int(counter)):
                dish_items = dict.fromkeys(['ingredient_name', 'quantity', 'measure'])
                ingredient = file_work.readline().strip().split(' | ')
                for item in ingredient:
                    dish_items['ingredient_name'] = ingredient[0]
                    dish_items['quantity'] = ingredient[1]
                    dish_items['measure'] = ingredient[2]
                list_of_ingredient.append(dish_items)
                cook_book = {dish_name: list_of_ingredient}
                menu.update(cook_book)
            file_work.readline()
    return menu


dict_collector('recipes.txt')


def get_shop_list_by_dishes(dishes, persons):
    menu = dict_collector('recipes.txt')
    shopping_list = {}
    for dish in dishes:
        for item in (menu[dish]):
            items_list = dict([(item['ingredient_name'], {'measure': item['measure'],
                                                          'quantity': int(item['quantity']) * persons})])
            if shopping_list.get(item['ingredient_name']):
                extra_item = (int(shopping_list[item['ingredient_name']]['quantity']) +
                              int(items_list[item['ingredient_name']]['quantity']))
                shopping_list[item['ingredient_name']]['quantity'] = extra_item
            else:
                shopping_list.update(items_list)

    pprint(shopping_list)


get_shop_list_by_dishes(['Омлет', 'Омлет'], 2)
