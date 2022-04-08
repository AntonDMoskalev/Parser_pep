# Парсер документации для языка Python.

## Технологии:
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)

## Описание проекта:

#### Парсер позволяет получить актуальную информацию о нововведениях в языке Python, получить данные о версиях (номера, статусы, ссылки на документацию), скачать документацию, узнать о статусах PEP — Python Enhancement Proposal.

## Запуск проекта:

#### Склонировать репозиторий
> https://github.com/AntonDMoskalev/bs4_parser_pep.git

#### Установить и активировать виртуальное окружение
> python -m venv venv

#### Обновить менеджер пакетов PIP
> pip install --upgrade pip

#### Requirements.txt
> pip install -r requirements.txt

## Функции и работа с командной строкой Парсера

#### whats_new - cобирает ссылки на статьи о нововведениях в Python. Формат вывода: Ссылка на статью, Заголовок, Редактор, Aвтор.
> python main whats_new

#### latest_versions - собирает информацию о версиях Python. Формат вывода: Ссылка на документацию, Версия, Статус.
> python main latest_versions

#### download - скачивает архив с документацией Python на ваш локальный диск.
> python main download

#### pep - собирает информацию о количестве PEP в каждом статусе и общее количество PEP.
> python main pep

#### Дополнительные аргументы
> -c, --clear-cache     Очистка кеша

#### Выбор способа выдачи результатов работы парсера(По умолчанию: построчно в терминале, pretty: таблично в терминале, file: файл .csv)
> -o {pretty,file}, --output {pretty,file}
