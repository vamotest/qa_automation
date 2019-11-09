from selenium import webdriver


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
        'http://eubelov1:PhgpeViAK8knGySJZPfb@hub.browserstack.com:80/wd/hub',
        desired_capabilities=desired_capabilities
    )

    return driver
