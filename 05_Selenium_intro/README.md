
* Установить opencart

```bash
curl -sSL https://raw.githubusercontent.com/bitnami/bitnami-docker-opencart/master/docker-compose.yml > docker-compose.yml
```
```bash
docker-compose up -d
```
* Написать фикстуру для запуска трех разных браузеров (Safari, Firefox, Chrome) в полноэкранном режиме с опцией headless. Выбор браузера должен осуществляться путем передачи аргумента командной строки pytest. По завершению работы тестов должно осуществляться закрытие браузера.
* Добавить опцию командной строки, которая указывает базовый URL opencart.
Написать тест, который открывает основную страницу opencart и проверяет, что мы находимся именно на странице приложения opencart.

```bash
http://<ip_or_fqdn>/opencart/
```

В качестве решения прислать ссылку на коммит и скриншот с успешным запуском тестов.