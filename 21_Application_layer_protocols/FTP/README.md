# Работа с сетью. Протоколы прикладкого уровня

```
1) Реализовать клиент, который будет подключаться по SSH и выполнять команды.
2) Настроить с помощью SSH-клиента FTP-сервер: 
2.1. установка (если не установлен); 
2.2. создание пользователя;
2.3. удаление пользователя
```
```
3) Реализовать FTP-клиент, который будет подключаться к FTP-серверу 
и сможет выполнять следующие действия: 
3.1. загружать файлы в папку; 
3.2. создавать папку;
3.3. удалять папку;
3.4. переходить по папкам
4) Должны обрабатываться исключения при попытке подключиться по FTP: 
4.1. пользователем, которого не существует
4.2. пользователем, с неверным логином и паролем
```

### How to use:
* Запустите docker image `bitnami/opencart:3` с перенаправлением портом:
```sh
~ docker run -p 4422:22 -p 8443:443 -p 8080:80 p 2121:21 -d bitnami/opencart:3
```
* Посмотрите список запущенных контейнеров:
```sh
~ docker ps
```
* Подключитесь к контейнеру:
```sh
~ docker exec -it {CONTAINER_ID} sh
```
* Выполните следующие команды в контейнере:
```sh
~ apt-get update
~ apt-get upgrade
~ apt-get install vsftpd nmap nano
```
* Создайте пользователя и выберите пароль, 
остальные данные можно оставить по умолчанию:
```sh
~ sudo adduser {usename}

Adding user `{usename}' ...
Adding new group `{usename}' (1007) ...
Adding new user `{usename}' (1006) with group `{usename}' ...
Creating home directory `/home/{usename}' ...
Copying files from `/etc/skel' ...
Enter new UNIX password:
Retype new UNIX password:
passwd: password updated successfully
Changing the user information for {usename}
Enter the new value, or press ENTER for the default
	Full Name []:
	Room Number []:
	Work Phone []:
	Home Phone []:
	Other []:
Is the information correct? [Y/n] Y
```
* Создайте каталог ftp, установите права на него и отнимите право на запись
 в этом каталоге:
```sh
~ sudo mkdir /home/{usename}/ftp
~ sudo chown nobody:nogroup /home/{usename}/ftp
~ sudo chmod a-w /home/{usename}/ftp
``` 
* Теперь создайте каталог для хранения файлов и передайте пользователю права
собственности на него:
```sh
~ sudo mkdir /home/{usename}/ftp/files
~ sudo chown {usename}:{usename} /home/{usename}/ftp/files
```
* Нужно отредактировать `vsftpd.conf` и заменить его содержимое следующим:
```sh
~ nano /etc/vsftpd.conf

... 
anonymous_enable=YES
local_enable=YES
write_enable=YES
local_umask=022
dirmessage_enable=YES
xferlog_enable=YES
connect_from_port_20=YES
xferlog_std_format=YES
nopriv_user=ftp
listen=YES
pam_service_name=vsftpd
userlist_enable=NO
tcp_wrappers=YES
check_shell=NO
ftp_username=ftp
...
```
* Cделайте рестарт службы `vsftpd`:
```sh
~ service vsftpd restart
```
* Теперь вы можете подключиться с локальной машины по FTP к контейнеру:
```sh
~ ftp localhost -p 2121

...
Connected to localhost.
220 (vsFTPd 3.0.3)
Name (localhost:name): {usename}
331 Please specify the password.
Password:
230 Login successful.
ftp> bye
221 Goodbye.
...
```