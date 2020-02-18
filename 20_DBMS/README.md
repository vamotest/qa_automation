# Работа с СУБД 

## Создание базы данных для логирования тестирования
```
Цель: Цель: научиться создавать бд и таблицы через pydb api поменять логгер из сохранения в файлы в сохранение бд можно поменять как глобальный logger, так и EventFiringDriver, если глобальный не настроен
Создать БД для логов (sqlite)
Переписать логгер из дз так, чтобы действия записывались в БД
```

## Подготовка тестовых данных для автотестов путём создания сущности в БД
```
1) Необходимо настроить подключение к базе данных Opencart 
(данные для подключения будут в opencart/config.php,
если не запомнили при создании контейнера/виртуалки)
Используется база mysql, поэтому нужен коннектор для нее. 
Можно использовать и pyodbc, и pymysql 

2) В одну из таблиц opencart добавить новую запись с вашими данными 
(oc_customers - клиенты, то есть создадим нового клиента) 

3) Написать тест, который использует эти данные. 
Например, с новым клиентом можно оформить заказ 

4) Удалить после выполнения теста созданные данные.
Написать коннектор к базе данных OpenCart.
Создать любую сущность через БД и написать тест проверки её создания
(через селениум)
```
## How to use
* В `docker-compose.yml` добавляем проброс портов к `mariadb`, 
чтобы иметь возможность подключаться к базе:
```
~ nano docker-compose.yml
```
```
version: '2'
services:
  mariadb:
    image: 'bitnami/mariadb:10.3'
    environment:
      - MARIADB_USER=bn_opencart
      - MARIADB_DATABASE=bitnami_opencart
      - ALLOW_EMPTY_PASSWORD=yes
    ports:
      - '3306:3306'
    volumes:
      - 'mariadb_data:/bitnami'
  opencart:
    ...
```
* Сборка и запуск docker-compose:
```shell script
~ docker-compose build docker-compose.yml
~ docker-compose up opencart mariadb 
```
* Запускаем тест:
```shell script
~ cd ../05_11_Selenium/tests 
~ python3 -m pytest 20_Database_connection_test.py [--browser] [--verbose]
```
* Arguments:
```sh
[--browser] (default="Chrome"): Chrome/Firefox/Safari
[--verbose]: increase verbosity
```