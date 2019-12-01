import os
import sys
import subprocess
import argparse
import json


def get_args():
    """Arguments parser"""
    args = argparse.ArgumentParser()

    args.add_argument('--package', type=str, default='setuptools',
                      help='Package name to show version')
    args.add_argument('--directory', type=str,  default='/Users/',
                      help='Directory to show files it contains')
    args.add_argument('--port', type=str, default='22',
                      help='Port number to show it\'s type')
    args.add_argument('--service', type=str, default='network',
                      help='Show service status')

    return args.parse_args()


def get_os_info():

    args = get_args()

    # Cетевые интерфейсы:
    network_interfaces = subprocess.check_output('netstat -i')

    # Маршрут по-умолчанию:
    default_path = os.getenv('PATH')

    # Информацию о состоянии процессора:
    cpu_info = subprocess.check_output(
        'sysctl -n machdep.cpu.brand_string'
    ).strip()

    # Информацию о процессе:
    process_id = os.getpid()

    # Список всех процессов:
    all_processes = subprocess.check_output('ps aux')

    # Статистику работы сетевых интерфейсов:
    interfaces_stat = subprocess.check_output('ifconfig')

    # Статус работы какого либо сервиса:
    service_status = subprocess.check_output(
        f'systemctl status {args.service}'
    )

    # Состояние сетевого порта на сервере(TCP или UDP):
    port_type = subprocess.check_output(
        f'nmap localhost | grep {args.port}'
    )

    # Версию пакета(имя пакета передается как аргумент):
    package_version = subprocess.check_output(
        f'pip freeze | grep {args.package}'
    )

    # Список в файлов в директории (указать директорию):
    files_list = os.listdir(args.directory)

    # Текущая директорию:
    current_directory = os.getcwd()

    # Версия ядра:
    python_core = sys.version.strip()

    # Версия операционной системы:
    os_information = f'{os.uname()[0]} {os.uname()[2]}'

    os_info = {
        'network_interfaces': network_interfaces,
        'default_path': default_path,
        'cpu_info': cpu_info,
        'process_id': process_id,
        'all_processes': all_processes,
        'interfaces_stat': interfaces_stat,
        'service_status': service_status,
        'port_type': port_type,
        'package_version': package_version,
        'files_list': files_list,
        'current_directory': current_directory,
        'python_core': python_core,
        'os_information': os_information,

    }

    with open('os_info.json', 'w+') as output:
        json.dump(os_info, output, indent=2)


if __name__ == '__main__':
    get_os_info()
