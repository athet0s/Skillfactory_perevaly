# Описание
Проект по виртуальной стажировке для курса Skillfactory  
Простой REST API для отправки информации о перевалах в базу данных

# Требования к среде
python 3.7  
pip  
postgreSQL  
psycopg2  
uvicorn

# Установка
1. После git clone установите необходимые зависимости через requirements.txt
```
pip install -r requirements.txt
```
2. Запустите sql скрипт perevaly_db_generation_script.sql для генерации структуры базы данных
3. В коренной дериктории создайте .env файл с следующими параметрами
```
FSTR_DB_NAME=<имя базы данных>
FSTR_DB_HOST=<хост базы данных>
FSTR_DB_LOGIN=<имя пользователя базы данных>
FSTR_DB_PASS=<пароль базы данных>
FSTR_DB_PORT=<порт подключения к базе данных>
```
4. Для запуска сервера использется uvicorn 
```
uvicorn main:app --host 0.0.0.0 --port 80
```

# Доступный функцианал  
swagger документация к API
```
GET /docs/
```
<br>
<br>
отправить информацию о перевале в базу данных

```
POST /submitData/
```
пример объекта запроса
```
{
  "title": "Пхия",
  "beauty_title": "пер. ",
  "other_titles": "Триев",
  "add_time": "2021-09-22 13:18:13",
  "connect": "",
  "user": {
    "email": "qwerty@mail.ru",
    "phone": "+7 555 55 55",
    "name": "Василий",
    "fam": "Пупкин",
    "otc": "Иванович"
  },
  "images": [
    {
      "title": "string",
      "data": "string"
    }
  ],
  "coords": {
    "height": "1200",
    "latitude": "45.3842",
    "longitude": "7.1525"
  },
  "level": {
    "winter": "",
    "summer": "1А",
    "autumn": "1А",
    "spring": ""
  }
}
```

объект ответа 
```
{"status": 200, "message": "Отправлено успешно", "id": added_pereval_id}
```
```status``` дублирует HTTP статус  
```message``` сообщение о результате запроса  
```id``` id созданного перевала при успешном запросе

<br>
<br>

получить информацию о перевале по id
```
GET /submitData/<id>
```
пример объекта ответа
```
{
  "id": 20,
  "date_added": "2022-11-30T15:43:47.965255",
  "status": "new",
  "beauty_title": "пер. ",
  "title": "Пхия",
  "other_titles": "Триев",
  "connect": "",
  "add_time": "2021-09-22T13:18:13",
  "level_winter": "",
  "level_summer": "1А",
  "level_autumn": "1А",
  "level_spring": "",
  "latitude": 45.3842,
  "longitude": 7.1525,
  "height": 1200
}
```

<br>
<br>


получить список перевалов по эмэйлу отправителя
```
GET /submitData/?user__email=<email>
```
пример объекта ответа
```
[
 {
    "id": 19,
    "title": "Анзоб",
    "beauty_title": "пер. ",
    "status": "new",
    "date_added": "2022-12-09T19:39:07.101576",
    "latitude": 33.4512,
    "longitude": 91.9214,
    "height": 2000
  },
  {
    "id": 20,
    "title": "Пхия",
    "beauty_title": "пер. ",
    "status": "new",
    "date_added": "2022-12-09T20:04:37.379822",
    "latitude": 45.3842,
    "longitude": 7.1525,
    "height": 1200
  }
]
```

