# Сайт лаборатории систем искусственного интеллекта
# Инструкция по развёртыванию на сервере 
***
## Инструкция работает со следующей конфигурацией:
* Ubuntu 22.04 LTS 64-bit
* Python 3.10
* Оперативная память >= 5Гб (рек. 8Гб)
* Дисковое хранилище >= 16Гб (рек. 20Гб)
* Ядра процессора >= 8 (рек. 12)
***
## Установка общих зависимостей
>```bash
>apt install git
>apt install python3.10-venv
>apt-get install ffmpeg libsm6 libxext6
>
>curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
>sudo apt install nodejs gcc g++ make -y
>```
***
## Установка бекенда на Джанго
1. Загрузка репозитория
>```Bash
>git clone https://github.com/hentaibaka/NUL-SII-site-backend.git
>```
2. Установка проекта
>```Bash
>cd NUL-SII-site-backend
>source setup/build.sh
>```
3. Медиа файлы
> Медиа файлы будут обрабатываться через ```Nginx```, 
