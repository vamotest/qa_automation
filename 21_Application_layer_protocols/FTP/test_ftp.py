from ftp_client import ftp_connect, ftp_authorization, ftp_client_finish


def test_ftp_login():

    # Подключаемся к FTP:
    ftp_connect()

    # Проходим аутентификацию:
    data_ftp_login = ftp.login(conf['user']['name'], conf['user']['password'])

    # Проверяем успешность авторизации:
    if 'Login' and 'successful' in data_ftp_login:
        print('Login successful')
    elif 'Login' and 'successful' not in data_ftp_login:
        assert False, 'Login incorrect. Verify user or password'
    else:
        assert False, 'Something wrong'

    # Завершаем подключение по FTP:
    ftp_client_finish()


def test_ftp_mkdir():

    # Авторизовываемся по FTP:
    ftp_authorization()

    # Создаем папку на удаленном сервере по указанному пути:
    data_ftp_mkdir = ftp.mkd(conf['user']['path_to_remote_folder'])

    # Проверяем, что папка была создана:
    if '257' and 'created' in data_ftp_mkdir:
        print('The folder was successfully created')
    elif '550' and 'failed' in data_ftp_mkdir:
        assert False, 'The folder was not successfully created'
    else:
        assert False, 'Something wrong'

    # Удаляем папку после проверки:
    print(ftp.rmd(conf['user']['path_to_remote_folder']))

    # Завершаем подключение по FTP:
    ftp_client_finish()
