# Бот викторина
У нас есть два бота: ```TelegramBot``` и ```VkontakteBot```, где вы можете принять участие в викторине.
Попробовать сыграть можно:
<br>
 ```TelegramBot``` - <a href='https://t.me/DevmanLesson3_bot'>здесь,</a>
 <br>
```VkontakteBot``` - <a href='https://vk.com/im?media=&sel=-190053871'>здесь.</a>

## Инструкция по запуску кода на сервере

### Регистрация и установка Heroku

Зарегистрируйтесь  на этом <a href='https://signup.heroku.com/dc'>сайте</a>.
<br>
Для работы через терминал, установите ```CLI``` для ```Heroku```, для этого
откройте у себя на компьютере ```bash``` и в нем пропишите следующие команды: 
<br>
Для ```Linux``` -<br>
```sudo snap install heroku --classic```
<br>
Для ```MacOs``` - <br>
```brew install heroku/brew/heroku```
<br>
Оставаясь в терминал, зайдите через ```bash``` в ваш аккаунт на ```Heroku```:
<br>
```heroku login```
<br>
### Загрузка кода на сервер Heroku

Загрузите с ```github``` ваш репозиторий на компьютер: 
<br>
```git clone https://github.com/djeck1432/quiz_bot.git```
<br>
Откройте папку:
<br>
```cd quiz_bot ```
<br>
Создайте приложения в ```Heroku``` :
<br>
```heroku create```
<br>
Загрузите ваш репозиторий на сервер ```Heroku```:
<br>
```git push heroku master```
<br>

### Настройка окружения и запуск сервера

Перейдите по <a href='https://dashboard.heroku.com/apps'>ссылке</a>, выберите свое приложение и откройте его.
<br>
В меню навигации, перейдите на вкладку ```Settings```.
<br>
В разделе ```Config vars```, передайте ваши переменные окружения.
<br>
В терминале, выполните следующую команду для запуска кода на сервере:<br>
```heroku ps:scale bot=1```
<br>
Поздравляю, теперь ваш ```Bot``` работает постоянно, вне зависимости, включен ваш компьютер или нет.
<a name='env'></a>

## Переменные окружения 

```TELEGRAM_ACCESS_TOKEN```- ```Telegram``` токен;
<br>
```VK_ACCESS_TOKEN```- ```Vkontakte``` токен;
<br>
Параметры базы данных ```Redis``` :
<br>
```REDIS_PASSWORD ```-  пароль;
<br>
```REDIS_PORT```- порт;
<br>
```REDIS_HOST```- хост;

## Пример работы ботов

<img src='https://dvmn.org/filer/canonical/1569215494/324/'>
