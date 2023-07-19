## Скрипт для получения уведомлений о выходе новых записей ВКонтакте в отслеживаемых группах в личные сообщения.


## Инструкции по установке
***- Клонируйте репозиторий:***
```
git clone git@github.com:misha7up/vk_new_post_announcer.git
```

***- Установите и активируйте виртуальное окружение:***
- для MacOS
```
python3 -m venv venv
```
- для Windows
```
python -m venv venv
source venv/bin/activate
source venv/Scripts/activate
```

***- Установите зависимости из файла requirements.txt:***
```
pip install -r requirements.txt
```

***- Как запустить парсер:***
- для MacOS
```
python3 parser.py
```
- для Windows
```
python parser.py