# Непрерывная интеграция [![Build Status](https://travis-ci.org/vamotest/qa_automation.svg?branch=26_Continuous_Integration)](https://travis-ci.org/vamotest/qa_automation)
* Запуск тестов через Travis CI
```
1) Использовав Selenium написать любые тест на любой сайт
2) Выложить на GitHub
3) Прикрутить запуски в Travis CI
4) Добавить в README.md бейджик build

Для запуска тестов можно использовать любой SaaS-grid
Сборка на Travis CI должна быть зеленая, в репозитории должен быть бейджик
```

### How to use:
* Необходимо авторизоваться в [Travis CI](https://github.com/login?client_id=f244293c729d5066cf27&return_to=%2Flogin%2Foauth%2Fauthorize%3Fclient_id%3Df244293c729d5066cf27%26redirect_uri%3Dhttps%253A%252F%252Fapi.travis-ci.org%252Fauth%252Fhandshake%26scope%3Dread%253Aorg%252Cuser%253Aemail%252Crepo_deployment%252Crepo%253Astatus%252Cwrite%253Arepo_hook%26state%3DldsGL5S0LK_xjZdvaXXYJA%253A%253A%253Ahttps%253A%252F%252Ftravis-ci.org%252F) под своей учеткой в GitHub
* В [настройках](https://travis-ci.org/account/repositories) аккаунта выбрать желаемый отслеживаемый репозиторий
* В разделе [Branches](https://travis-ci.org/vamotest/qa_automation/branches) выбрать желаемую отслеживаемую ветку, по-умолчанию `master`
* Создадим `.travis.yml` в корне репозитория, указав данные для сборки
* Ранее мы использовали SaaS-grid, а именно `BrowserStack`, то в `.travis.yml`
для запуска тестов будем указывать: 
```
script:
    - run pytest 13_Selenium_remote_start/BrowserStack/test_remote_grid.py
```
* Так как в тестах используется `url` c личными данными для доступа 
к `BrowserStack`, то необходимо добавить данные параметры 
в `Environment Variables` в [настройках](https://travis-ci.org/vamotest/qa_automation/settings) вашего репозитория
При запуске тестов в логах информация о параметрах будет отображаться:
```
Setting environment variables from repository settings
$ export protocol=[secure]
$ export login=[secure]
$ export password=[secure]
$ export host=[secure]
$ export port=[secure]
$ export hub=[secure]
``` 