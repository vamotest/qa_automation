import sys
sys.path.insert(0, "playground/21_Application_layer_protocols/SSH")
from ssh_client import ssh_authorization, ssh_client_finish
import yaml

conf = yaml.safe_load(open('ftp_user_configuration.yml'))


def test_is_vsftpd_installed():

    # Авторизовываемся по SSH:
    ssh_authorization()

    stdin, stdout, stderr = client.exec_command('dpkg -s vsftpd')
    is_vsftpd_installed = stdout.read() + stderr.read()

    if "Status" and "installed" in is_vsftpd_installed.decode():
        print('The vsftpd package has been installed')
    elif "Status" and "installed" not in is_vsftpd_installed.decode():
        stdin, stdout, stderr = client.exec_command('apt-get install vsftpd')
        is_vsftpd_installed_now = stdout.read() + stderr.read()
        if "vsftpd" and "newly installed" in is_vsftpd_installed_now():
            print('The vsftpd package is just installed now')
        else:
            assert False, 'The vsftpd package has not been installed now'
    else:
        assert False, 'Something wrong'

    # Завершаем подключение по SSH:
    ssh_client_finish()


def test_is_user_created():
    # Авторизовываемся по SSH:
    ssh_authorization()

    # Создаем пользователя:
    client.exec_command('sudo adduser ' + conf['user']['name'])
    client.exec_command(conf['user']['password'])
    client.exec_command(conf['user']['retype_password'])
    client.exec_command(conf['user']['full_name'])
    client.exec_command(conf['user']['room_number'])
    client.exec_command(conf['user']['work_phone'])
    client.exec_command(conf['user']['home_phone'])
    client.exec_command(conf['user']['other'])

    # Подтверждаем, что данные введены корректно:
    client.exec_command(conf['user']['is_information_correct'])

    # Создаем каталог ftp:
    client.exec_command('sudo mkdir /home/' + conf['user']['name'] + '/ftp')

    # Устанавливаем права на него:
    client.exec_command(
        'sudo chown nobody:nogroup /home/' + conf['user']['name'] + '/ftp'
    )

    # Отнимием право на запись в этом каталоге:
    client.exec_command(
        'sudo chmod a-w /home/' + conf['user']['name'] + '/ftp'
    )

    # Cоздаем каталог для хранения файлов:
    client.exec_command(
        'sudo mkdir /home' + conf['user']['name'] + '/ftp/files'
    )

    # Передаем пользователю права собственности на него:
    client.exec_command(
        'sudo chown ' + conf['user']['name'] + ':' + conf['user']['name']
        + '/home/' + conf['user']['name'] + '/ftp/files'
    )

    # Проверяем, что пользователь есть в списке FTP пользователей:
    stdin, stdout, stderr = client.exec_command('cat /etc/vsftpd.userlist')
    is_user_created = stdout.read() + stderr.read()

    if conf['user']['name'] in is_user_created.decode():
        print('User is successfully created')
    elif conf['user']['name'] not in is_user_created.decode():
        assert False, 'User is not successfully created'
    else:
        assert False, 'Something wrong'

    # Завершаем подключение по SSH:
    ssh_client_finish()


def test_is_user_deleted():

    # Авторизовываемся по SSH:
    ssh_authorization()

    # Проверяем, что пользователь есть в списке FTP пользователей
    stdin, stdout, stderr = client.exec_command('cat /etc/vsftpd.userlist')
    is_user_created = stdout.read() + stderr.read()

    # Удаляем пользователя
    client.exec_command('sudo userdel ' + conf['user']['name'])

    if conf['user']['add'] not in is_user_created.decode():
        print('User is successfully deleted')
    elif conf['user']['add'] not in is_user_created.decode():
        assert False, 'User is not successfully deleted'
    else:
        assert False, 'Something wrong'

    # Завершаем подключение по SSH:
    ssh_client_finish()
