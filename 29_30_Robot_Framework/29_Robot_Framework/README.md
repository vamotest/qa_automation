## Введение в Robot Framework 
```
Использование RobotFramework
Цель: Научиться запускать тесты RobotFramework
1. Настроить работу с RobotFramework
2. Написать тесты для администраторской панели на RobotFramework 
(выбрать самостоятельно 3 кейса)
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
* Устанавливаем зависимости:
```shell script
~ pip install -r requirements.txt
```
* Запускаем тесты:
```shell script
~ robot test_admin_page.robot
```
* После выполнения теста в текущей директории создадутся файлы `output.xml`, 
`log.html`, `report.html`