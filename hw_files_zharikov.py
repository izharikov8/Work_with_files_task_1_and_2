from pprint import pprint
import os

path = os.path.join(os.getcwd(), 'recepies.txt')

with open(path, encoding='utf8') as f:
    cook_book = {}
    for dish in f:
        dish_name = dish.strip()
        counter = int(f.readline().strip())
        temp_data = []
        for item in range(counter):
            name, qty, measure = f.readline().strip().split('|')
            temp_data.append({'name': name, 'qty': int(qty), 'measure': measure})
        cook_book[dish_name] = temp_data
        f.readline()

# pprint(cook_book)


def get_shop_list(dishes, persons):
    res = {}
    for x in dishes:
        for y in cook_book[x]:
            if y['name'] in res.keys():
                res[y['name']]['qty'] += y['qty']
            else:
                res[y['name']] = {}
                res[y['name']]['measure'] = y['measure']
                res[y['name']]['qty'] = y['qty'] * persons
    return res

pprint(get_shop_list(['Запеченный картофель', 'Омлет', 'Фахитос'], 3))



