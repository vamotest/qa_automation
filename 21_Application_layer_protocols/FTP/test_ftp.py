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


def test_ftp_rmdir():

    # Авторизовываемся по FTP:
    ftp_authorization()

    # Создаем папку для теста:
    ftp.mkd('delete')

    # Проверяем файлы и папки в текущей директории:
    data_before_rmdir = ftp.retrlines('LIST')

    # Удаляем папку:
    ftp.rmd('delete')

    # Проверяем файлы и папки в текущей директории после удаления:
    data_after_rmdir = ftp.retrlines('LIST')

    # Проверяем, что данные в директории до и после удаления отличаются:
    if ('delete' in data_before_rmdir) and ('delete' not in data_after_rmdir):
        print('The folder was successfully deleted')
    elif 'delete' in (data_before_rmdir and data_after_rmdir):
        assert False, 'The folder was not successfully deleted'
    else:
        assert False, 'Something wrong'

    # Завершаем подключение по FTP:
    ftp_client_finish()


def test_ftp_cd():

    # Авторизовываемся по FTP:
    ftp_authorization()

    data_cd = ftp.cwd((conf['user']['path_to_remote_folder']))

    if 'successfully' and 'changed' in data_cd:
        print('Directory was successfully changed')
    elif 'Failed' and 'to change' in data_cd:
        assert False, 'Directory was not successfully changed'
    else:
        assert False, 'Something wrong'

    # Завершаем подключение по FTP:
    ftp_client_finish()


def test_ftp_put():

    # Авторизовываемся по FTP:
    ftp_authorization()

    # Переходим в папку на удаленном сервере, куда мы хотим загрузить файл:
    ftp.cwd(conf['user']['path_to_remote_folder'])

    # Загружаем файл с локальной системы на удаленный сервер:
    with open(conf['user']['remote_file'], 'r') as file:
        data_put = ftp.storlines('STOR' + conf['user']['local_file'], file)

    # Проверяем корректность загрузки файла на удаленный сервер:
    if 'Transfer' and 'complete' in data_put:
        print('The file was successfully uploaded')
    elif 'Transfer' and 'complete' in data_put:
        assert False, 'The file was not successfully uploaded'
    else:
        assert False, 'Something wrong'

    # Удаляем после теста файл
    ftp.rmd(conf['user']['remote_file'])

    # Завершаем подключение по FTP:
    ftp_client_finish()
