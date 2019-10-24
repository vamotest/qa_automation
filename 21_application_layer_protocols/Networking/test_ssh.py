import yaml
import time
import paramiko


conf = yaml.safe_load(open('configuration.yml'))
client = paramiko.SSHClient()


def ssh_authorization():
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        hostname=conf['credentials']['hostname'],
        username=conf['credentials']['username'],
        password=conf['credentials']['password'],
        port=conf['credentials']['port']
    )


def ssh_client_finish():
    client.close()


def test_restart_service():
    ssh_authorization()
    stdin, stdout, stderr =\
        client.exec_command(
            'export PATH=$PATH:/sbin:/bin:/usr/bin:/usr/sbin:/usr/local/sbin:/'
            'usr/local/bin && echo '' | sudo -S /etc/init.d/dbus restart'
        )
    data_restart_service = stdout.read() + stderr.read()
    if "Starting" and "done" in data_restart_service.decode("utf-8"):
        print('Service was successfully restart')
    elif "Starting" and "done" not in data_restart_service.decode("utf-8"):
        print('Service was not successfully restart')
    else:
        print('Something wrong')


def test_reboot_system():
    ssh_authorization()
    stdin, stdout, stderr = client.exec_command('last reboot')
    data_before_reboot = stdout.read() + stderr.read()
    print(data_before_reboot.decode("utf-8"))
    client.exec_command('echo '' | sudo -S reboot -f')
    ssh_client_finish()

    time.sleep(10)

    ssh_authorization()
    stdin, stdout, stderr = client.exec_command('last reboot')
    data_after_reboot = stdout.read() + stderr.read()
    print(data_after_reboot.decode("utf-8"))
    ssh_client_finish()

    if data_before_reboot != data_after_reboot:
        print('System was successfully reboot')
    elif data_before_reboot == data_after_reboot:
        print('System was not successfully reboot')
    else:
        print('Something wrong')


