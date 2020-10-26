# Интерактивная карта Москвы

<img src="screenshots/site.gif"/>

Данный проект поможет создать интерактивную карту, на которой будут фото с подробными описаниями и комментариями.

Содержит в себе удобный для заполнения данных интерфейс, а так же возможность массово загружать данные в формте `.json`.

Посмотреть пример: http://antaurendev.pythonanywhere.com/

## Запуск

- Скачайте код
- Установите зависимости  
  ```
  pip install -r requirements.txt
  ```

- Создайте БД 
  ```
  python3 manage.py migrate
  ```
- Запустите сервер командой 
  ```
  python3 manage.py runserver
  ```

## Как добавить данные
(Положить файлы с данными в папку *places/data* в формате *.json*)
- Добавить **все** данные: запустите команду 
  ```
  python3 manage.py load_place --all
  ```
- Добавить отдельные файлы: запустите команду 
  ```
  python3 manage.py load_place --files example_1.json example_2.json
  ```

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. 
Чтобы их определить, создайте файл `.env` рядом с `manage.py` 
и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 3 переменные:
- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python 
и веб-разработке на сайте [Devman](https://dvmn.org/modules/django/lesson/yandex-afisha).
