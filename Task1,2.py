
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

class YaUploader:

    def __init__(self, token):
        self.token = token


    def upload(self, file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
        params = {"path": file_path, "owerwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()


    def upload_to_disk(self, file_path, filename):
        href = self.upload(file_path=file_path).get('href', '')
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()



if __name__ == '__main__':

    with open('1.txt', 'r') as f:
        token = f.readline().rstrip()
        uploader = YaUploader(token)
        pprint(uploader.upload_to_disk('netology/3.txt', '3.txt'))