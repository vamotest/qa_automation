import time
from ssh_client import ssh_authorization, ssh_client_finish


def test_restart_service():

    # Авторизовываемся по SSH:
    ssh_authorization()

    # Выполняем restart сервиса dbus
    stdin, stdout, stderr = client.exec_command(
        'sudo -S /etc/init.d/dbus restart'
    )
    data_restart_service = stdout.read() + stderr.read()

    # Проверяем был ли сервис dbus перезапущен
    if "Starting" and "dbus" in data_restart_service.decode():
        print('Service was successfully restarted')
    elif "Starting" and "dbus" not in data_restart_service.decode():
        assert False, 'Service was not successfully restarted'
    else:
        assert False, 'Something wrong'

    # Завершаем подключение по SSH:
    ssh_client_finish()


def test_reboot_system():

    # Авторизовываемся по SSH:
    ssh_authorization()

    # Проверяем, когда была последняя перезагрузка системы
    stdin, stdout, stderr = client.exec_command('last reboot')
    data_before_reboot = stdout.read() + stderr.read()
    print(data_before_reboot.decode())

    # Перезагружаем систему
    client.exec_command('sudo -S reboot -f')

    # Завершаем подключение по SSH:
    ssh_client_finish()

    # Ожидаем перезагрузку системы
    time.sleep(20)

    # Авторизовываемся по SSH:
    ssh_authorization()

    # Проверяем, когда была последняя перезагрузка системы
    stdin, stdout, stderr = client.exec_command('last reboot')
    data_after_reboot = stdout.read() + stderr.read()
    print(data_after_reboot.decode())

    # Проверяем была ли действительна перезагружена система
    if data_before_reboot != data_after_reboot:
        print('System was successfully rebooted')
    elif data_before_reboot == data_after_reboot:
        assert False, 'System was not successfully rebooted'
    else:
        assert False, 'Something wrong'

    # Завершаем подключение по SSH:
    ssh_client_finish()
