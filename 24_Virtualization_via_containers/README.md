# Виртуализация. Контейнеры 
```
Сборка собственного контейнера.
Необходимо собрать собственный докер контейнер, в котором будет код тестового фреймворка (последний) из репозитория на github и установлены все необходимые зависимости для старта тестов.
```

### How to use:
* Авторизовываемся в Docker Hub
```sh
~ docker login
...
Login with your Docker ID to push and pull images from Docker Hub. If you don't have a Docker ID, head over to https://hub.docker.com to create one.
Username:
Password: 
Login Succeeded
...
```
* Собираем Dockerfile, который находится в директории 
```sh
~ docker build -t my_repo:v.0.1 . 
...
Successfully built {ID}
...
```
```sh
docker tag {ID} vamotest/my_repo:v.0.1
```
* Отправляем в репозиторий на Docker Hub:
```sh
~ docker push vamotest/my_repo:v.0.1
...
The push refers to repository [docker.io/python_automation/my_repo]
...
v.0.1: digest: sha256:{SHA_ID} size: 4947
```
* Теперь другие пользователи могу скопировать себе образ:
```sh
~ docker pull vamotest/my_repo
```