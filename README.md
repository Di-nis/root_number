# Root Number


## Описание
REST API-сервис Root Number - сервис по нахождению корня числа.
http://127.0.0.1:8000/swagger/ - документация
http://127.0.0.1:5555/ - мониторинг


## Развертывание

1. Docker-compose up
2. Запуск Redis - docker run -d -p 6379:6379 redis;
3. Запуск Celery - celery -A api worker --loglevel=INFO
4. Запуск Flower - flower -A api --port=5555

## Создано с помощью

* [Django](https://docs.djangoproject.com/en/3.1/) - Python веб фреймворк
* [Django REST framework](https://www.django-rest-framework.org/) - 
Библиотека для создания REST-сервисов на основе Django


## Авторы, контактная информация

* **Денис Смирнов** - *Team leader, разработчик* - (https://github.com/Di-nis)
Электронная почта - di-nis@yandex.ru

