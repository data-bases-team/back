Скачаем код:
```
git clone https://github.com/data-bases-team/back.git
cd back
```



при необходимости поменять порт в DOCKERFILE и docker-compose.yml

```
docker pull docker.io/library/python:3.9   
sudo docker-compose build
sudo docker-compose up
```

Ваш сайт будет по адресу:
`virtual.fn11.bmstu.ru:{ваш порт}`

Админка тут: 
`virtual.fn11.bmstu.ru:{ваш порт}/admin`


в запросе от пользователя будет название контейнера и еще какая то чертовщина, порт берем ближайший свободный
1. при добавлении нового юзера надо создать в корне проекта создаем новую попку с названием от юзера <str> и кидаем в нее копию ./db/db.sqlite3
2. в docker-compose добавляем новое приложение по шаблону
```
  <str>:
    image: back-master:0.0.1
    build: .
    volumes:
      - ./<str>:/app/db
    ports:
      - "<ближайший свободный порт, или не ближайший мне похуй>:8000"
    container_name: <str>
    command: python manage.py runserver 0.0.0.0:8000
```

- чтобы все это дело поднять пишем 
```
docker compose up
```
чтобы помониторить залупку
```
docker ps
```
убиваем конкретный контейнер
```
docker rm -f <str>
```
останавливаем докер
```
docker compose down
```

заходим в консоль конкретного экземпляра приложения
```
docker compose exec <str> bash
```

смотрим логи , ьщжно ебануть флаг -f <str>, чтобы логи только конкретного приложения глянуть
```
docker compose logs
```

Чтобы создать нового пользователя (при необходимости использовать совместно с `docker compose exec`):
```
python3 manage.py createsuperuser
```

Для нового сайтика нужно прописать новую папку-прокси в nginx:
```
location /menu/static {
        proxy_pass http://localhost:8000/menu/static;
}
location /menu/images {
        proxy_pass http://localhost:8000/menu/images;
}
location /menu {
        proxy_pass http://localhost:8000/;
}
``` 

Для создания нового контейнера можно испольщзрвать скрипт:
```
./new_container.sh app_name
sudo service nginx 
```