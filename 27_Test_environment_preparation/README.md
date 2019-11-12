# Подготовка тестового окружения 
```
Сборка wheel тестового фреймворка
Добавить setup.py для тестового фреймворка.
Тесты работают после установки из .whl файла.
```

### How to use:
* Файлы `__init__.py` необходимы для того, чтобы Python трактовал эти каталоги
 как содержащие пакеты
* `setup.py` должен находится в корне репозитория
* Необходимо обновить `setuptools` and `wheel`: 
```sh
~ python3 -m pip install --user --upgrade setuptools wheel
```
* Для выполнении сборки:
```sh
~ python3 setup.py sdist bdist_wheel
```
* Эта команда должна выводить много текста и после ее завершения генерировать
два файла в каталоге dist:
```
dist/
  qa_automation-0.1-py3-none-any.whl
  qa_automation-0.1.tar.gz
```
* Обновляем `pip` до актуальной версии:
```sh
~ pip install --upgrade pip
```
* Пакет можно установить из `PyPI` (предварительно необходимо загрузить) или
локально из файла:
```sh
~ pip install qa_automation-0.1-py3-none-any.whl
```
* Для запуска тестов выполняем команду:
```sh
~ python3 -m pytest -s -v
```