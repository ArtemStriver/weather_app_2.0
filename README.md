# weather_app_2.0

______
**weather_app_2.0** - консольная программа для получения погоды по IP адресу
устройства пользователя. Проект выполнен по материалам Алексея Голобурдина в
качестве получения навыков написания правильного кода с использованием
типизации.

***Функционал программы:***

Запуская программу в терминале, будет выведена следующая информация:

``` tmux
Город, температура, тип_погоды
Время_восхода
Время_заката

   ||  ||  || 
   \/  \/  \/
   
Москва, температура +18°C, Ясно
Восход: 06:34
Закат: 22:49
```

Также данные о погоде сохраняются в текстовый или JSON файл.

## Установка и запуск

Скачиваем репозиторий со всеми файлами с GitHub. После этого необходимо
в файл `config.py`, расположенный в папке `settings`, написать свой персональный
api-ключ от сайта [openweathermap](https://openweathermap.org/), его
можно бесплатно получить после регистрации на этом сайте.

После этого можно запустить файл `weather` и узнать погоду.

Для пользователей UNIX систем (Linux/MacOS) можно прописать в терминале следующие
команды:

``` python
cd `путь_до_файла_weather`    # переходим в директорию с файлом

chmod +x weather                   # делаем файл исполняемым

sudo ln -s $(pwd)/weather /usr/local/bin/ # добавляем файл в корень системы, 
                                          # чтобы его можно было вызывать откуда угодно 
                                          # (в пределах системы)
```

После чего можно запускать программу простым вводом в терминал `weather`.

В каталоге с программой есть файл `requirements.txt`, библиотеки их него
можно не устанавливать (там находиться только mypy), они нужны только для
проверки правильности типизации.

## Используемые технологии

![version](https://img.shields.io/badge/python-3.10-blue)

![license](https://img.shields.io/badge/license-Apache__License__V2.0-green)

## Лицензия

Проект разработан с использованием лицензии [Apache License, Version 2.0](https://opensource.org/license/apache-2-0/)
