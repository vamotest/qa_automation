# Selenium

## Index
* [How to use](#How_to_use)
* [Основы Selenium](#Основы_Selenium)
* [Поиск элементов ](#Поиск_элементов)

### How to use
* Создайте виртуальное окружение и активируйте его:
```sh
~ python3 -m venv env && source env/bin/activate
```
* Обновите pip до последней версии:
```sh
~ pip install --upgrade pip
```
* Установите зависимости:
```sh
~ pip install -r requirements.txt
```

* Скачайте docker-image `Opencart` и запустите его:
```sh
~ curl -sSL https://raw.githubusercontent.com/bitnami/bitnami-docker-opencart/master/docker-compose.yml > docker-compose.yml
~ docker-compose up -d
```

**[⬆ Back to Index](#index)**
### Основы Selenium

```
Установить opencart

Написать фикстуру для запуска трех разных браузеров (Chrome, Firefox, Safari)
в полноэкранном режиме с опцией headless. 

Выбор браузера должен осуществляться путем передачи аргумента командной строки.
По завершению работы тестов должно осуществляться закрытие браузера.

Добавить опцию командной строки, которая указывает базовый URL opencart.
Написать тест, который открывает основную страницу opencart и проверяет, 
что мы находимся именно на странице приложения opencart.
```

* Запускаем тесты:
```sh
~ pytest test_selenium.py [--opencart_url] [--browser] [--verbose]
~ python3 -m pytest 05_Selenium_intro_test.py --url="http://localhost/index.php" --browser=Firefox --verbose
```

* Arguments:
```sh
[--browser] (default="Chrome"): Chrome/Firefox/Safari
[--opencart_url] (default="http://localhost:80/"): http://localhost/index.php
[--verbose]: increase verbosity
```

**[⬆ Back to Index](#index)**
### Поиск элементов 

```
1. Описать элементы на страницах: 
- Главная (Шапка, разделы меню, промоблок, футер, поисковая строка)
- Карточка товара 
- Раздел каталога
- Панель логина /admin/

2. Реализовать 5 тестовых сценариев, в основе которых будут лежать поиск 
элементов и элементарные действия (click, submit, input) и задействованы 
все описанные страницы

Требования:
Тесты проходят в браузерах Firefox, Chrome, Safari - опционально.
Локаторы используются из отдельного пакета с локаторами.
Тесты независимы друг от друга.
```

* Запускаем тесты:
```sh
~ python3 -m pytest 06_Searching_elements_test.py [--browser] --verbose
```