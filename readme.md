# Дипломный проект QA.GURU
___
        
## Объект тестирования
Для теста было выбрано два сайта, [Регард](https://www.regard.ru/) и мобильное приложение магазина [Все инструменты](https://www.vseinstrumenti.ru/) 
___
![This is an image](readme_files/regard-scaled.jpg)
## Что тестируется
Основные виды тестирования (WEB и API) будут проводиться на сайте Регард  
### WEB-тестирование

- Авторизация пользователя с валидными данными
- Авторизация пользователя с невалидными данными
- Успешный логаут пользователя
- Поиск предмета в каталоге
- Добавление предмета в корзину
- Изменение количества предметова в корзине
- Удаление предмета из корзины

### API-тестирование

- Авторизация пользователя с валидными данными
- Авторизация пользователя с невалидными данными
- добавление предмета в корзину
- Удаление предмета из корзины

**Мобильные тесты проводятся на мобильном приложении Все инструменты**

### Мобильное тестирование  

- Поиск предмета в каталоге
- Добавление предмета в корзину
- Удаление предмета из корзины
___
### Используемый стек:  
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-plain-wordmark.svg" height="40" width="40" /> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/selenium/selenium-original.svg" height="40" width="40" /> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/chrome/chrome-original-wordmark.svg" height="40" width="40" /> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-original.svg" height="40" width="40" /> <img src="https://avatars.githubusercontent.com/u/5879127?s=200&v=4" width="40" height="40"/> <img src="https://raw.githubusercontent.com/Vyroum/Vyroum/refs/heads/main/icons/icons8-telegram.svg" width="40" height="40"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytest/pytest-original.svg" width="40" height="40"/> 
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/browserstack/browserstack-original.svg" height="40" width="40" /> 

  
___ 

### Запуск проекта автотеста в Jenkins:
1. Откройте [проект](https://jenkins.autotests.cloud/job/c17_vyroum_diploma_work//)
2. Выберите ``Build with parameters``
3. Измените параметры, если требуется
4. Нажмите ``Build``


>**Доступные параметры**:
>- ENVIRONMENT: selenoid, browserstack
>- TEST: web, api, mobile  
На селеноиде возможен запуск только web и api тестов  
>На browserstack возможен запуск только mobile тестов

### Запуск проекта автотеста локально:
1. Скорпировать репозиторий
2. Запустить через терминал, использую команду ``pytest --context={ENVIRONMENT} -m {TEST}`` где ENVIRONMENT=окружение, например `local`, а TEST= вид теста, например `web`
3. Сгенерировать отчёт, используя команду ``allure serve .\allure-result\``
___
## Пример отчёта в Allure

### Общий отчёт о пройденном тесте
<img src="https://github.com/Vyroum/Vyroum/blob/main/icons/Screenshot_1.png" width="630" height="320"/>

### Детальный отчёт о пройденном тесте

<img src="https://github.com/Vyroum/Vyroum/blob/main/icons/Screenshot_3.png" width="630" height="320"/>

### Видеопрохождение теста

<img src="https://github.com/Vyroum/Vyroum/blob/main/icons/5d0f6222e058a005354e5f9b95638274.gif" width="630" height="320"/>

### Отчёт о прохождении теста в Telegram

<img src="https://github.com/Vyroum/Vyroum/blob/main/icons/Screenshot_2.png" width="300" height="320"/>
