# Index
1. [How to use](#how-to-use)
2. [Основы Selenium](#selenium-intro)
3. [Поиск элементов](#searching-elements)
4. [Работа с элементами](#work-with-elements)
5. [Действия с элементами](#actions-with-elements)
6. [Ожидание элементов](#waiting-for-elements)
7. [PageObject](#page-object)
8. [Работа с окнами](#work-with-windows)


## How to use
* Создайте виртуальное окружение и активируйте его:
```shell script
~ python3 -m venv env && source env/bin/activate
```
* Обновите pip до последней версии:
```shell script
~ pip install --upgrade pip
```
* Установите зависимости:
```shell script
~ pip install -r requirements.txt
```

* Скачайте docker-image `Opencart` и запустите его:
```sh
~ curl -sSL https://raw.githubusercontent.com/bitnami/bitnami-docker-opencart/master/docker-compose.yml > docker-compose.yml
~ docker-compose up -d
```


**[⬆ Back to Index](#index)**
## Основы Selenium

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
```shell script
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
## Поиск элементов

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
```shell script
~ python3 -m pytest 06_Searching_elements_test.py [--browser] --verbose
```


**[⬆ Back to Index](#index)**
## Работа с элементами

```
Для страницы Products реализовать тесты, которые проверяют 
функциональность добавления, изменения и удаления продукта

Требования:
Тесты проходят в браузерах Firefox, Chrome.
Отсутствуют дублирующиеся и захардкоженные локаторы в методах.
Тесты независимы друг от друга.
Код легко поддерживать и изменять
```
* Запускаем тесты:
```shell script
~ python3 -m pytest 07_Work_with_elements_test.py [--browser] --verbose
```


**[⬆ Back to Index](#index)**
## Действия с элементами
```
Цель: Научиться работать с ActionChains
1. Зайти на сайт https://code.makery.ch/library/dart-drag-and-drop/
2. В Examples-Basic сложить все иконки документов в корзинку
```
* Запускаем тесты:
```shell script
~ python3 -m pytest 08_Actions_with_elements_test.py [--browser] --verbose
```

**[⬆ Back to Index](#index)**
## Ожидание элементов
```
Добавить ожидание элементов
Цель: Тесты проходят в браузерах firefox, chrome. 
Отсутствуют дублирующиеся и захардкоженные локаторы в методах. 
Тесты независимы друг от друга. Код легко поддерживать и изменять.

1. Добавить ожидания элементов и обработку исключений для тестов страницы 
Products
2. Добавить ожидание в настройки браузера перед тестом
3. Добавить опцию выставления ожидания для браузера в опции командной строки
```
* Запускаем тесты:
```shell script
~ python3 -m pytest 09_Waiting_for_elements_test.py [--browser] [--implicitly_wait] --verbose
```
* Arguments:
```sh
[-implicitly_wait] (default="60"): Implicit browser timeout in seconds
```

**[⬆ Back to Index](#index)**
## Работа с окнами
```
Реализовать загрузку файла:
1) В админ панели в разделе Catalog -> Downloads есть форма для загрузки файлов
Нужно, реализовать загрузку файлов через эту форму.
```
* Запускаем тесты:
```shell script
~ python3 -m pytest 11_Work_with_windows_test.py [--browser] [--implicitly_wait] --verbose
```