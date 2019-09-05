# Основы Selenium

* Установить opencart
* Написать фикстуру для запуска трех разных браузеров (Chrome, Firefox, Safari) в полноэкранном режиме с опцией headless. Выбор браузера должен осуществляться путем передачи аргумента командной строки pytest. По завершению работы тестов должно осуществляться закрытие браузера.
* Добавить опцию командной строки, которая указывает базовый URL opencart.
* Написать тест, который открывает основную страницу opencart и проверяет, что мы находимся именно на странице приложения opencart.

В качестве решения прислать ссылку на коммит и скриншот с успешным запуском тестов.

### How to use:
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

* Скачайте образ opencart
```sh
~ curl -sSL https://raw.githubusercontent.com/bitnami/bitnami-docker-opencart/master/docker-compose.yml > docker-compose.yml
~ docker-compose up -d
```

* Запустите тесты

```sh
# from downloaded directory
~ pytest test_selenium.py [--browser] [--opencart_url] [--verbose]
~ pytest test_selenium.py --browser=Chrome --opencart_url="http://localhost/index.php" --verbose
```

### Arguments:
```sh
--browser (default="Chrome"): Chrome/Firefox/Safari
--opencart_url (default="http://localhost:80/"): http://localhost/index.php
--verbose: increase verbosity
```

