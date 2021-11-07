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


def get_shop_list_by_dishes(dishes, person_count):
    order = {}
    for dish in dishes:
        counter = dishes.count(dish)
        if dish in cook_book:
            for i in cook_book[dish]:
                if counter == 1:
                    order[i['ingredient_name']] = {
                        'measure': i['measure'], 'quantity': (int(i['quantity']) * person_count)}
                else:
                    order[i['ingredient_name']] = {
                        'measure': i['measure'], 'quantity': (int(i['quantity']) * counter)}
    return order


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
