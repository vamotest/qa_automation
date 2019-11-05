# Работа с сетью. Протоколы низкого уровня

```
1. Сделать http клиент на базе библиотеки сокет.
2. Клиент должен принимать как аргументы метод, url, хост, заголовки 
и возвращать текст ответа в виде строки, код ответа, заголовки.
По сути нужно продублировать функцинальность библиотеки requests (GET запросы)
Ограничения: пользуемся только библиотекой socket
```

### How to use:
* Запускать командой:
```sh
~ python3 -m pytest test_socket_client.py -s -v
```
* При возникновении ошибки `error [SSL: CERTIFICATE_VERIFY_FAILED] certificate 
verify failed`:
```sh
Applications → Python {version}
...
DoubleClick → Install Certificates.command
DoubleClick → Update Shell Profile.command
...
```

