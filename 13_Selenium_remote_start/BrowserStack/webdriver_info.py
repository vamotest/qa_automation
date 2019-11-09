import os
from selenium import webdriver

protocol = os.environ['protocol']
login = os.environ['login']
password = os.environ['password']
host = os.environ['host']
port = os.environ['port']
hub = os.environ['hub']


def remote_driver():

    desired_capabilities = {
        'browser': 'Firefox',
        'browser_version': '70.0 beta',
        'os': 'Windows',
        'os_version': '10',
        'resolution': '2048x1536',
        'name': 'Sample Test'
    }

    driver = webdriver.Remote(
        command_executor=
        protocol + '://' + login + ':' + password + '@' + host + ':' + port + '/' + hub,
        desired_capabilities=desired_capabilities
    )

    return driver


