# Bot quiz
We have two bots: `TelegramBot` and `VkontakteBot`, where you can take part in a quiz. You can try playing:

`TelegramBot` - <a href='https://t.me/DevmanLesson3_bot'>here,</a>

`VkontakteBot`- <a href='https://vk.com/im?media=&sel=-190053871'>here.</a>
## An example of the work of bots

<img src='https://dvmn.org/filer/canonical/1569215494/324/'>


## Instruction for running code on the server

### Registration and installation of Heroku

Sign up on this  <a href='https://signup.heroku.com/dc'>site</a>.
<br>
To work through the terminal install `CLI` for `Heroku`, to do this you should open `bash` on your computer and write in there next commands: 
<br>
For Linux  `Linux` -
```
sudo snap install heroku --classic
```
For `MacOs` - 
```
brew install heroku/brew/heroku
```
Staying in the terminal, log into your account on `Heroku` with `bash`:
```heroku login```
<br>
### Download code on Heroku

Download from `github` your repository to computer:
```
git clone https://github.com/djeck1432/quiz_bot.git
```
Open the folder:
```
cd quiz_bot
```
Create a new app on `Heroku` :
```
heroku create
```
Download your repository on the server `Heroku`:
```
git push heroku master
```

### Setting up the environment and starting the server

Go to the <a href='https://dashboard.heroku.com/apps'>link</a>, choose your app and open it.

In the navigation menu, go to the tab `Settings`.

In chapter `Config vars`, pass your environment variables.

In the terminal, do the next command for start code on the server:

`heroku ps:scale bot=1`

Congratulations, now your `Bot` is constantly working.

<a name='env'></a>

## Environment variables 

`TELEGRAM_ACCESS_TOKEN`- `elegram` token;

`VK_ACCESS_TOKEN`- `Vkontakte` token;

Database options `Redis`:

`REDIS_PASSWORD`-  password;

`REDIS_PORT`- port;

`REDIS_HOST`- host;


