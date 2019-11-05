from socket_client import ssl_create, socket_create, socket_connect, \
    request_create, socket_send, socket_receive, close_connect
import yaml

conf = yaml.safe_load(open('configuration.yml'))

method = conf['request']['method']
port = conf['request']['port']
host = conf['request']['host']
headers = conf['request']['headers']


def test_get_response():
    # Создаем SSL-подключение:
    context = ssl_create()

    # Cоздаем Socket-client:
    sock = socket_create(context, host)

    # Подключаемся к серверу:
    socket_connect(sock, host, port)

    # Создаем запрос:
    request = request_create(method, host, headers)

    # Отправляем запрос:
    sock = socket_send(sock, request)

    # Ответ читается порциями по 4096 байт (или 4 кб):
    response_data = socket_receive(sock)

    # Проверяем, что мы получили успешный ответ:
    if 'HTTP/1.1' and '200' and 'OK' in response_data:
        print(f'{method}: The resource has been fetched and is transmitted'
              f' in the message body\n', response_data)
    elif ('HTTP/1.1' and '200' and 'OK') not in response_data:
        assert False, '400 Bad Request '
    else:
        assert False, 'Something wrong'

    # Закрываем соединение:
    close_connect(sock)
