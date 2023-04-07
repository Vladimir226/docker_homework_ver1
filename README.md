# О приложении:
реализован простой пример из документации по созданию веб-сервера на flask.
# Использование:
  - переходим в необходимую директорию (pwd - текущий путь cd example/directory/ - переход по пути)
  - создаем образ с помощью команды:   `docker build . -t my_docker_flask:latest -f Dockerfile`
  - создаем контейнер с помощью команды: `docker run -d -p 5000:5000 my_docker_flask:latest`
  - переходим на сервер: http://127.0.0.1:5000/
