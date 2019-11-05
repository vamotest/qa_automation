import socket
import ssl


def ssl_create():
    # Создаем SSL-подключение:
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.verify_mode = ssl.CERT_REQUIRED
    context.check_hostname = True
    context.load_default_certs()
    return context


def socket_create(context, host):
    # Создаем Socket-клиент:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock = context.wrap_socket(sock, server_hostname=host)
    return sock


def socket_connect(sock, host, port):
    # Подключаемся к серверу:
    sock.connect((host, port))


def request_create(method, host, headers):
    # Создаем запрос:
    request = f'{method} / HTTP/1.1\n\n' + f'Host: {host}\n\n' + f'{headers}'
    return request


def socket_send(sock, request):
    # Отправляем запрос:
    sock.send(request.encode())
    return sock


def socket_receive(sock):
    # Ответ читается порциями по 4096 байт (или 4 кб):
    response = sock.recv(4096)
    return response.decode()


def close_connect(sock):
    # Закрываем соединение:
    sock.close()
