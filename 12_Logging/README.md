# Протоколирование

```
Настроить протоколирование проекта

1 балл - за настроенный event_firing_webdriver (в том числе снятие скриншотов при падениях драйвера)
1 балл - запись лога в файл
1 балл - работа с логом с помощью модуля logging
1 балл - снятие логов с браузера
1 балл - настройка логирования http запросов через proxy
```
* Запускаем новые тесты:
```shell script
~ cd 05_11_Selenium/tests
~ python3 -m pytest 12_Work_with_elements_test.py [--browser] --verbose
```
* Arguments:
```sh
[--browser] (default="Chrome"): Chrome/Firefox/Safari
[--verbose]: increase verbosity
```