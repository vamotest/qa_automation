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
