# VST-Blog

### О проекте
Это простой блог для создания и просмотра блоговых постов с возможностью их комментировать. Ресурс состоит из бэкенда и фронтенда.


## Backend

### Используется:

- Python
- Django
- PostgreSQL


### Перед началом работы:

#### Установка зависимостей:

В корневой папке находиться файл с зависимостями requirements.txt
```shell
pip install -r backend_blog/requirements.txt
```

#### Развертывание базы данных:

Для удобства развертывания базы данных есть файл docker-compose 

````shell
docker-compose up -d db
````

#### Настройка переменных окружения:

Для работы проекта необходимо создать **.env** в папке backend_blog/.
В нем нужно указать необходимые значения переменных:

* DEBUG=True (или False) - **включения или выключения дебагера django**
* SECRET_KEY = **секретный ключ**
* DB_HOST = хост базы данных
* DB_PORT = порт базы данных
* DB_USER = имя пользователя базы данных
* DB_PASSWORD = пароль от базы данных
* DB_NAME = имя базы
* TIME_ZONE = по умолчанию "UTC"

### Запуск проекта Django:

* Перед запуском проекта, накатываем миграции на базу данных командой

```shell
python ./manage.py migrate
```
* Запуск проекта

```shell
python ./manage.py runserver
```

* Загрузка тестовых данных (по желанию)
```shell
python ./manage.py loaddata ./datajson/testdata.json
```

## Frontend

### Используется

- JavaScript
- Nuxt3
- TailwindCSS

### Шаг 1: Установка зависимостей
Перед запуском приложения, необходимо установить все зависимости.
Для этого откройте терминал и перейдите в директорию проекта **./frontend_blog** . Затем выполните команду:

```shell
npm install
```

### Шаг 2: Запуск приложения в режиме разработки
После установки зависимостей, можно запустить приложение в режиме разработки. Для этого выполните команду:
```shell
npm run dev
```
Эта команда запустит приложение на локальном сервере по адресу http://localhost:3000/. Приложение будет автоматически перезагружаться при внесении изменений в код.

### Шаг 3: Сборка и запуск приложения в продакшн
Когда вы закончите разработку и готовы запустить приложение в продакшн, выполните следующие команды:

```shell
npm run build
npm run start
```

Команда npm run build создаст оптимизированные версии файлов приложения в директории dist. Команда npm run start запустит приложение на локальном сервере в режиме продакшн по адресу http://localhost:3000/.

## Запуск через Docker compose
В корневой папке находиться docker-compose.yaml для запуска проекта на локальной машине.

```shell
docker compose up -d
```


# Проект доступен в облаке по адресу https://158.160.58.142/