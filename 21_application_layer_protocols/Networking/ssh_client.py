import yaml
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
