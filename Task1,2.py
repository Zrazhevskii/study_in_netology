
#--------------------------------ЗАДАНИЕ1-------------------------------------
from pprint import pprint
import requests

TOKEN = '2619421814940190'
urls = [
    f'https://www.superheroapi.com/api.php/{TOKEN}/search/Hulk',
    f'https://www.superheroapi.com/api.php/{TOKEN}/search/Thanos',
    f'https://www.superheroapi.com/api.php/{TOKEN}/search/Captain%America',
]


def requests_get(url_all):
    r = (requests.get(url) for url in url_all)
    return r

def parser():
    # функция парсинга интелекта
    super_man = []
    for item in requests_get(urls):
        intelligence = item.json()
        try:
            for power_stats in intelligence['results']:
                super_man.append({
                    'name': power_stats['name'],
                    'intelligence': power_stats['powerstats']['intelligence'],
                })
        except KeyError:
            print(f"Проверте ссылки urls: {urls}")

    intelligence_super_hero = 0
    name = ''
    for intelligence_hero in super_man:
        if intelligence_super_hero < int(intelligence_hero['intelligence']):
            intelligence_super_hero = int(intelligence_hero['intelligence'])
            name = intelligence_hero['name']

    print(f"Самый интелектуальный {name}, интелект: {intelligence_super_hero}")

parser()


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