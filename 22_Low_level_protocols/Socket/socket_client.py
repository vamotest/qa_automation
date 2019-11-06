import socket
import ssl
import time

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


# def socket_receive(sock):
#     # Ответ читается порциями по 4096 байт (или 4 кб):
#     response = sock.recv(2048)
#     return response.decode()


def socket_receive(sock):
    # Конец ответа, до которого будем искать:
    end_response = b'</html>'

    # Итоговый ответ:
    total_response = []

    while True:
        response = sock.recv(8192)
        if end_response in response:
            total_response.append(response[:response.find(end_response)])
            break
        total_response.append(response)
        if len(total_response) > 1:
            # Проверяем, если end_response был разбит
            last_pair = total_response[-2] + total_response[-1]
            if end_response in last_pair:
                total_response[-2] = last_pair[:last_pair.find(end_response)]
                total_response.pop()
                break
    return ''.join(str(x) for x in total_response)


def close_connect(sock):
    # Закрываем соединение:
    sock.close()
