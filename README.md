Настройка

- Пропишите необходимые переменные из .env-sample
- Установите виртуальное окружение и необходимые зависимости poetry install
- создайте и примените миграции:
    - python manage.py makemigrations
    - python manage.py migrate
- создайте суперпользвателя командой: python manage.py csu

- Загрузите данные online_platform в свою БД командой: python manage.py loaddata online_platform.json (возможно потребуется поменять кодировку файла json на UTF-8)

- Запустите приложение командой python manage.py runserver

- заходим в админку http://127.0.0.1:8000/admin, учетные данные 
    - email='admin@a.com'
    - password: admin

- в постман можно проверить контроллеры https://www.postman.com/

- необходимо обязательно получить токен и внести его в запросе Postman в "headers", ключ: "Authorization" т.к. контроллеры доступны авторизированным активным пользователям, кроме UserCreateApiView 