# BWT_TEST
Задание:

Спарсить данные с yelp.com по заданной категории и локации.
Тестово: 3 категории для 3 локаций с yelp.com
локации: LA, NY, SF
категории restaurants, gym, spa
Поля, которые необходимо сохранить: тайтл, адрес, телефон, имейл (если есть), вебсайт, расписание работы, описание (about), кол-во отзывов, ссылка на изображение (1 первое/главное)
Результаты парсинга сохранять в БД (mysql)
Категорию и локацию получать как параметры командной строки.
Использовать:
- python 3.7
- pipenv для виртуального окружения
- framework scrapy 
- sqlalchemy и alembic для создания таблиц и работы с бд. записи в бд не должны дублироваться при повторных парсингах 
- реализовать middleware для подключения прокси. обрабатывать ошибки (статус код) 429

###### Запуск:

`scrapy crawl test -a category=_category_ -a location=_location_`

где `_category_` - название категории. Может принимать значения _**restaurants**_, **_gym_** или **_spa_**

`_location_` - название локации. Может принимать значения **_LA_**, **_NY_**, **_SF_**

Проверку разрешенных значений категории и локации можно отключить, закоментировав строки
`ENABLED_LOCATIONS` и `ENABLED_CATEGORIES` в файле `bwt_test/settings.py`

###### Прокси:

По умолчанию подключен прокси. 

`DOWNLOADER_MIDDLEWARES = {

    ...
    'bwt_test.middlewares.ProxyMiddleware': 100,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
}`

При чем каждый новый запрос будет отправлен с нового прокси.
Адреса прокси-серверов содержатся в списке `PROXY_LIST` в файле `bwt_test/settings.py`

###### Обработка 429 статуса:

`DOWNLOADER_MIDDLEWARES = {
    
    ...
    'bwt_test.middlewares.Response429RetryMiddleware': 90,
    ...
}`

Если прокси подключен - просто делает запрос с нового адреса, иначе ждет 60 секунд, и снова посылает запрос.

###### Конфигурация подключения к БД:

`CONNECTION_STRING = "{drivername}://{user}:{passwd}@{host}:{port}/{db_name}?charset=utf8".format(
    
    drivername="mysql",
    user="demo",
    passwd="demodemo",
    host="localhost",
    port="3306",
    db_name="bwt_test",
)`

###### URL and Selector XPtahes:

`XPATHES` в `bwt_test/settings.py`
