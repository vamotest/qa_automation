import time
from ssh_client import ssh_authorization, ssh_client_finish


def test_restart_service():
    ssh_authorization()
    stdin, stdout, stderr = client.exec_command(
        'sudo -S /etc/init.d/dbus restart'
    )
    data_restart_service = stdout.read() + stderr.read()
    if "Starting" and "dbus" in data_restart_service.decode("utf-8"):
        print('Service was successfully restart')
    elif "Starting" and "dbus" not in data_restart_service.decode("utf-8"):
        assert False, 'Service was not successfully restart'
    else:
        assert False, 'Something wrong'


def test_reboot_system():
    ssh_authorization()
    stdin, stdout, stderr = client.exec_command('last reboot')
    data_before_reboot = stdout.read() + stderr.read()
    print(data_before_reboot.decode("utf-8"))
    client.exec_command('sudo -S reboot -f')
    ssh_client_finish()

    time.sleep(20)

    ssh_authorization()
    stdin, stdout, stderr = client.exec_command('last reboot')
    data_after_reboot = stdout.read() + stderr.read()
    print(data_after_reboot.decode("utf-8"))
    ssh_client_finish()

    if data_before_reboot != data_after_reboot:
        print('System was successfully reboot')
    elif data_before_reboot == data_after_reboot:
        assert False, 'System was not successfully reboot'
    else:
        assert False, 'Something wrong'
