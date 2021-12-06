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
    pprint(menu)
    return menu


dict_collector('recipes.txt')
