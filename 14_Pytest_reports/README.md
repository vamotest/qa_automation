## Pytest-отчёты
```
Расширить отчет pytest-plugin путем сбора инфы информации:
о установленных пакетах и переменных окружения
```

## How to use
* Добавляем `pytest-html` в `requirements.txt`
```shell script
~ nano requirements.txt
```
```
pytest-html
```
* Устанавливаем `pytest-html`
```shell script
~ pip install -r requirements.txt
```
* Редактируем `.gitignore ` и добавляем
```shell script
~ nano .gitignore 
```
```
# logs
/logs/

# reports
/assets/
/report/
report.html
```
* Редактируем `conftest.py` и добавляем
```shell script
~ nano conftest.py
```
```
import os

def _pytest_configure_(config):
    config.metadata['os'] = os.name
    config.metadata['PATH'] = os.environ['PATH']
    config.metadata['pwd'] = os.getcwd()
```
* Запускаем тесты
```shell script
~ python3 -m pytest -v --html=report.html
```
* Открываем `report.html`
```shell script
~ open report.html
```
```
Package: {'pytest': '5.3.2', 'py': '1.8.0', 'pluggy': '0.13.1'}
Platform: Darwin-18.7.0-x86_64-i386-64bit
Plugins: {'html': '2.0.1', 'metadata': '1.8.0'}
Python:	3.7.0
```