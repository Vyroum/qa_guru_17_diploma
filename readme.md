# Дипломный проект QA.GURU
___
        
## Объект тестирования
Для теста было выбрано два сайта, [Регард](https://www.regard.ru/) и мобильное приложение магазина [Все инструменты](https://www.vseinstrumenti.ru/) 
___
![This is an image](readme_files/regard-scaled.jpg)
## Что тестируется  
___  
## Веб-сайт "Регард"

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
- Добавление предмета в корзину
- Удаление предмета из корзины

## Мобильное приложение "Все инструменты"

### Мобильное тестирование  

- Поиск предмета в каталоге
- Добавление предмета в корзину
- Удаление предмета из корзины
___
### Используемый стек:  
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-plain-wordmark.svg" height="40" width="40" /> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/selenium/selenium-original.svg" height="40" width="40" /> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/chrome/chrome-original-wordmark.svg" height="40" width="40" /> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-original.svg" height="40" width="40" /> <img src="https://avatars.githubusercontent.com/u/5879127?s=200&v=4" width="40" height="40"/> <img src="https://raw.githubusercontent.com/Vyroum/Vyroum/refs/heads/main/icons/icons8-telegram.svg" width="40" height="40"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytest/pytest-original.svg" width="40" height="40"/> 
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/browserstack/browserstack-original.svg" height="40" width="40" /> <img src="https://github.com/Vyroum/qa_guru_17_diploma/blob/main/readme_files/default.svg" height="40" width="40" /> 

  
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
2. Запустить через терминал, используя команду ``pytest --context={ENVIRONMENT} -m {TEST}`` где ENVIRONMENT=окружение, например `local`, а TEST= вид теста, например `web`
3. Сгенерировать отчёт, используя команду ``allure serve .\allure-result\``
___
## Пример отчёта в Allure Report

### Общий отчёт о запущенных тестах
<img src="https://github.com/Vyroum/qa_guru_17_diploma/blob/main/readme_files/Screenshot_4.png" width="630" height="320"/>

### Детальный отчёт о пройденном тесте

<img src="https://github.com/Vyroum/qa_guru_17_diploma/blob/main/readme_files/Screenshot_7.png" width="630" height="320"/>

## Пример отчёта в Allure TestOps

### Общий отчёт о запущенных тестах  

<img src="https://github.com/Vyroum/qa_guru_17_diploma/blob/main/readme_files/Screenshot_1.png" width="630" height="320"/>

### Детальный отчёт о запущенных тестах

<img src="https://github.com/Vyroum/qa_guru_17_diploma/blob/main/readme_files/Screenshot_2.png" width="630" height="320"/>

## Видео примеры прохождения тестов

### Прохождение web-теста на добавление предмета в корзину 

<img src="https://github.com/Vyroum/qa_guru_17_diploma/blob/main/readme_files/6f6d5b7e7b992fb8a92a4a906d1ae56f.gif" width="630" height="320"/>

### Прохождение мобильного теста в приложении "Все инструменты"

<img src="https://github.com/Vyroum/qa_guru_17_diploma/blob/main/readme_files/video-e86e5a2bb5f578d50c260ad8fc6a7dda395b4854.gif" width="700" height="630"/>


## Отчёт о прохождении теста в Telegram

<img src="https://github.com/Vyroum/qa_guru_17_diploma/blob/main/readme_files/Screenshot_6.png" width="520" height="520"/>
