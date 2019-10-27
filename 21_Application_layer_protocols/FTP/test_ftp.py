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
