from setuptools import setup, find_packages

setup(
    name='qa_automation',
    version='0.1',
    url='https://github.com/vamotest/qa_automation',
    license='MIT',
    author='vamotest',
    author_email='vamotest@gmail.com',
    description='Python QA Engineer',
    packages=find_packages(exclude=['test']),
    install_requires=[
        'pandas==0.25.3',
        'paramiko==2.6.0',
        'pytest==4.6.0',
        'pyyaml==5.4',
        'selenium==3.141.0'
    ],
    zip_safe=False
)
