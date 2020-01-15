# RaspberryTank
Принцип работы :

запуск проекта python3 init.py
Для малины потребуется установить библиотеки/программы с помощью команд:

1) питон : sudo apt-get install python3
2) необходимый модуль : sudo apt install python3-pip
3) модуди работы с пинами :sudo pip3 install RPIO
4) фласк(API для для запуска сервера) : sudo apt-get install flask

Как работает:
1) Запуск с файла ____init____.py - на малине запускается сервер
2) На сайте есть кнопки(в случае необходимости можно добавить новых и действие к ним). Обмен между сервером и клиентом с помощью Post/get запроса.
3) Сервер получает число (но в случае необходимости переделывается под json-файлы) . За это отвечает функция led(state)
4) Клиент получает ответ в формате json-файла(функция ответственная за это switch() )

!!!!Необходимая мера,это протестить на получения большого количества запросов. Необходимость доработать механизм восстановления связи с бд в случае ошибки!!!!
