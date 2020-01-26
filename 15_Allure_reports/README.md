## Allure-отчёты
```
1. Промаркировать свои тесты
2. Добавить маркирование от allure к тестам
3. Сгенерировать отчет allure
```

## How to use
* Устанавливем и обновляеем `allure` через менеджер пакетов `brew`:
```shell script
~ brew install allure
~ brew upgrade allure
```
* Добавляем `allure-pytest` в `requirements.txt`:
```shell script
~ nano requirements.txt
```
```
allure-pytest
```
* Устанавливаем `allure-pytest`:
```shell script
~ pip install -r requirements.txt
```
* Запускаем тесты и указываем директорию для `allure`-отчета:
```shell script
~ python3 -m pytest test_brewery_api.py -v --alluredir=/tmp/my_allure_results
```
* Формируем html–отчет:
```shell script
allure serve /tmp/my_allure_results
```
* Press <Ctrl+C> to exit