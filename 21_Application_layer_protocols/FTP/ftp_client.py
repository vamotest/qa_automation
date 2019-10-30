from ftplib import FTP as ftp
import yaml

conf = yaml.safe_load(open('configuration.yml'))


# Подключаемся к FTP:
def ftp_connect():
    ftp.connect(conf['user']['host'], conf['user']['port'])


# Авторизовываемся по FTP:
def ftp_authorization():
    ftp.connect(conf['user']['host'], conf['user']['port'])
    print(ftp.login(conf['user']['name'], conf['user']['password']))


# Завершаем подключение по FTP:
def ftp_client_finish():
    print(ftp.quit())
