## Расширенное использование Robot Framework 

```
Расширенное использование RobotFramework
Цель: Научиться писать собственные модули для RobotFramework на Python
1. Добавить в Jenkins плагин Robotframework
1.1. Создать job для запуска тестов Robotframework
2. Написать библиотеку кейвордов для пользовательской части opencart
2.2. Написать 3 теста на RobotFramework используя написанные кейворды в п.2
```

## How to use
* Добавляем пакет [robotframework](https://pypi.org/project/robotframework/) в `requirements.txt`:
```shell script
~ nano requirements.txt
```
```
robotframework==3.1.2
```
* Добавляем пакет [selenium2library](https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html) для управления браузером в `requirements.txt`:
```shell script
~ nano requirements.txt
```
```
robotframework-selenium2library==3.0.0
```
* Скачиваем [Jenkins](https://jenkins.io/):
```shell script
~ wget -O jenkins.war http://ftp-chi.osuosl.org/pub/jenkins/war-stable/2.204.1/jenkins.war
```
* Запускаем `Jenkins` локально:
```shell script
~ java -jar jenkins.war
```
* Устанавливаем `Robot Framework plugin`:
```
Настроить Jenkins -> Управление плагинами -> Доступные -> Robot Framework plugin
```
* Создаем `Item`:
```
Введите имя Item'а -> {Item_name} -> Создать задачу со свободной конфигурацией -> OK
```
* Настраиваем сборку `выполнить команду shell`:
```
git clone https://github.com/vamotest/qa_automation.git
cd qa_automation/29_30_Robot_Framework/
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
robot 29_30_Robot_Framework/30_Extended_Robot_Framework/
```
* Сохранить
* Собрать сборку
* Смотрим результаты в разделе `Вывод консоли`