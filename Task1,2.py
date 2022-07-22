from pprint import pprint

def read_cook_book(file):
    data = {}
    key = ['ingredient_name', 'quantity', 'measure']
    with open(file, 'r', encoding='utf-8') as f:
        while True:
            ingredients = []
            name = f.readline().rstrip()
            if not name:
                break
            ingredient_count = f.readline().rstrip()
            for i in range(int(ingredient_count)):
                ing = f.readline().rstrip()
                ing_list = ing.strip().split("|")
                ingredient = dict(zip(key, ing_list))
                ingredient['quantity'] = int(ingredient['quantity'])
                ingredients.append(ingredient)
            data[name] = ingredients
            f.readline().rstrip()
    return data

file = 'data.txt'
data = read_cook_book(file)
pprint(data)

#---------------------------- ЗАДАЧА 2 -------------------------------------

def get_shop_list_by_dishes(dishes, person):
    cook_dict = {}
    for dish in dishes:
        if dish in data:
            for ingress_diets in data[dish]:
                dict_ing = {}
                if ingress_diets['ingredient_name'] in cook_dict:
                    quantity = cook_dict[ingress_diets['ingredient_name']].get('quantity') + \
                               ingress_diets['quantity'] * person
                    cook_dict[ingress_diets['ingredient_name']].update(quantity=quantity)
                else:
                    dict_ing['measure'] = ingress_diets['measure']
                    dict_ing['quantity'] = ingress_diets['quantity'] * person
                    cook_dict[ingress_diets['ingredient_name']] = dict_ing
    return cook_dict


pprint(get_shop_list_by_dishes({'Омлет', 'Фахитос', 'Запеченный картофель'}, 4))