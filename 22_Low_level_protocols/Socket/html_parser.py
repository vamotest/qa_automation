from socket_client import ssl_create, socket_create, socket_connect, \
    request_create, socket_send, socket_receive, close_connect
from abc import ABC
from collections import Counter
from html.parser import HTMLParser
import yaml

conf = yaml.safe_load(open('configuration.yml'))

method = conf['request']['method']
port = conf['request']['port']
host = conf['request']['host']
headers = conf['request']['headers']


class Parser(HTMLParser, ABC):

    # Задаем списки:
    tags = []
    links = []
    images = []
    text = []

    # Используем методы HTML Parser:

    def handle_starttag(self, start_tag, attrs):
        # Парсим все теги:
        self.tags.append(start_tag)
        # Парсим ссылки:
        if start_tag == 'a':
            attr = dict(attrs)
            self.links.append(attr['href'])
        # Парсим изображения:
        elif start_tag == 'img':
            attr = dict(attrs)
            self.images.append(attr['src'])

    def handle_data(self, data):
        # Парсим текст в тегах:
        self.text.append(data)


def main():
    """
    Точка входа
    """

    # Создаем SSL-подключение:
    context = ssl_create()

    # Создаем Socket-client:
    sock = socket_create(context, host)

    # Подключаемся к серверу:
    socket_connect(sock, host, port)

    # Создаем запрос:
    request = request_create(method, host, headers)

    # Отправляем запрос:
    sock = socket_send(sock, request)

    # Получаем ответ:
    parser = Parser()
    response_data = socket_receive(sock)
    parser.feed(response_data)

    # Парсим данные в интересующие нас списки:
    tags = Counter(parser.tags)
    text = list(parser.text)
    popular_tag = sorted(Counter(parser.tags).items(), key=lambda k: k[1])
    links = list(parser.links)
    images = list(parser.images)

    # Создаем словарь с результами:
    result = {
        'all_tags': tags,
        'text': text,
        'popular_tag': popular_tag[-1],
        'links': links,
        'images': images
    }

    # Выводим список тегов и их названия:
    print('\nAll tags:')
    for tag in list(result['all_tags']):
        print(tag)

    # Выводим текст на странице:
    print('\nText in tags:')
    for text in result['text']:
        print(text)

    # Выводим самый частовстречающийся тег:
    print('\nMost popular tag:', result['popular_tag'])

    # Выводим список ссылок на странице:
    print('\nLinks:')
    for link in result['links']:
        print(link)

    # Выводим список картинок на странице:
    print('\nImages:')
    for image in result['images']:
        print(image)


# Для запуска скрипта из командной строки:
if __name__ == '__main__':
    main()
