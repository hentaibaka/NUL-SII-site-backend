# NUL-SII-site-backend
## REST API для сайта НУЛ СИИ ИКИТ СФУ
### Требования к ПО:
1. Python=3.10
### Как запустить:
1. Установить виртуальное окружение
> Powershell:
> ```powershell
> py -3.10 -m venv venv
> ```

> Bash:
> ```bash
> python3.10 -m venv venv
> ```
2. Активировать виртуальное окружение
> Powershell:
> ```powershell
> ./venv/scripts/activate.ps1
> ```

> Bash:
> ```bash
> source venv/bin/activate
> ```
3. Обновить pip
> Powershell:
> ```powershell
> python -m pip install --upgrade pip
> ```

> Bash:
> ```bash
> -
> ```
4. Установить библиотеки
> Powershell:
> ```powershell
> pip install -r requirements.txt
> ```

> Bash:
> ```bash
> -
> ```
5. Сделать миграции
> Powershell:
> ```
> python manage.py migrate
> ```

> Bash:
> ```
> -
> ```
6. Создать суперпользователя
> Powershell:
> ```
> python manage.py createsuperuser
> ```

> Bash:
> ```
> -
> ```
7. Запустить тестовый сервер:
>Powershell:
>```
>python manage.py runserver
>```

> Bash:
> ```
> -
> ```
