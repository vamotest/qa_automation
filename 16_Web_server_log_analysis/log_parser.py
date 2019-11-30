from collections import Counter
from operator import itemgetter
import argparse
import os
import re
import sys
import json
import shutil


def get_args():
    """
    Парсер параметров из командной строки
    """
    arg_parser = argparse.ArgumentParser(description='access.log parser')

    arg_parser.add_argument('-f', '--file', type=str, dest='file',
                            help='Enter path to file')
    arg_parser.add_argument('-d', '--directory', type=str, dest="directory",
                            help='Enter path to files')
    return arg_parser.parse_args()


def read_file(input_file, output_file):
    """

    input_file : str
        Path to logs file.
    output_file : str
        Path to file  results.
    """

    requests_count = 0

    post_count = 0
    get_count = 0
    put_count = 0
    delete_count = 0
    head_count = 0
    patch_count = 0
    connect_count = 0
    options_count = 0
    trace_count = 0

    requests_list = []
    ip_list = []

    # Открытие файла с логами и чтение line by line
    try:
        with open(input_file, 'r', encoding='utf-8') as log:
            for line in log:

                # Счетчик HTTP методов:
                requests_count += 1

                if re.search('POST', line):
                    http_method = 'POST'
                    post_count += 1
                elif re.search('GET', line):
                    http_method = 'GET'
                    get_count += 1
                elif re.search('PUT', line):
                    http_method = 'PUT'
                    put_count += 1
                elif re.search('DELETE', line):
                    http_method = 'DELETE'
                    delete_count += 1
                elif re.search('HEAD', line):
                    http_method = 'HEAD'
                    head_count += 1
                elif re.search('PATCH', line):
                    http_method = 'PATCH'
                    patch_count += 1
                elif re.search('CONNECT', line):
                    http_method = 'CONNECT'
                    connect_count += 1
                elif re.search('OPTIONS', line):
                    http_method = 'OPTIONS'
                    options_count += 1
                elif re.search('TRACE', line):
                    http_method = 'TRACE'
                    trace_count += 1

                # Использование регулярных выражений для поиска информации:
                request_ip = re.match(
                    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line
                )
                request_duration = re.search(r'(\d)*$', line)
                request_url = re.search(r'(/\D*) HTTP', line)
                request_status_code = re.search(r'(\d{3}) ', line)

                if request_ip and request_duration \
                        and request_url and request_status_code:
                    requests_list.append(
                        [
                            request_ip.group(0),
                            request_duration.group(0),
                            http_method,
                            request_url.group(1),
                            request_status_code.group(1)
                        ]
                    )
                    ip_list.append(request_ip.group(0))

    # Возникает, когда файл не указан при вызове из командной строки:
    except TypeError:
        sys.exit('Log file not defind. Use argument "--file=filename"')

    # Возникает, когда запрашиваемый файл не существует:
    except FileNotFoundError:
        sys.exit('Unable to open log file, check your file\'s directory')

    # Топ-10 IP-адресов, с которых поступали запросы:
    top_requests = list(
        sorted(Counter(ip_list).items(), key=lambda x: x[1], reverse=True)
    )[:9]

    # Топ-10 IP-адресов, по продолжительности запросов:
    top_duration = sorted(requests_list, key=itemgetter(1), reverse=True)[:9]

    # Топ-10 запросов с ошибками клиента (4**):
    top_client_error = [x for x in requests_list if x[4].startswith('4')][:9]

    # Топ-10 запросов с ошибками сервера (5**):
    top_server_error = [x for x in requests_list if x[4].startswith('5')][:9]

    # Формируем структуру файла с результатами:
    result = {
        'requests':
            {
                'all': requests_count,
                'post_count': post_count,
                'get_count': get_count,
                'put_count': put_count,
                'delete_count': delete_count,
                'patch_count': patch_count,
                'connect_count': connect_count,
                'options_count': options_count,
                'trace_count': trace_count,
             },
        'top_requests': top_requests,
        'top_duration': top_duration,
        'top_client_error': top_client_error,
        'top_server_error': top_server_error
    }

    # Создаем файл с результатами и записываем данные c двойнным отступом:
    try:
        with open(output_file, 'w+') as output:
            json.dump(result, output, indent=2)
    except Exception as exc:
        sys.exit(f'Unable to write file: {exc}')


def read_dir(directory):
    """
    directory : str
        Path to directory with logs files
    """

    # Проверяем, существует ли указанная директория:
    if os.path.exists(directory):

        # Проверяем, является ли указанный путь директорией:
        if os.path.isdir(directory):

            # Cписок файлов и директорий в папке:
            files = os.listdir(directory)

            for file in files:

                f_name = file.split('.')[0]

                # Проверяем, что файл является log'ом:
                if file.endswith('.log'):
                    read_file(
                        os.path.join(directory, file),
                        f'result_log_{f_name}.json'
                    )

        else:
            sys.exit(f'{directory} - is not directory')
    else:
        sys.exit(f'{directory} - no such directory exists')


def main():
    """
    Точка входа
    """
    args = get_args()

    if args.directory:
        read_dir(args.directory)

        # Удаляем директорию с логами после тестового прогона:
        shutil.rmtree(args.directory)
    else:
        f_name = args.file.split('.')[0]
        read_file(args.file, output_file=f'result_log_{f_name}.json')

        # Удаляем лог-файл после тестового прогона:
        os.remove(args.file)


if __name__ == '__main__':
    main()
