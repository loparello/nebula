# Nebula

## About
Nebula is a simple and open source starter kit for Django apps and websites development. 

The idea comes mostly from the necessety to have frequently used apps - like pages or blog - already built in when starting a new project. The other necessity was to make the front-end development in Django apps modern and not relying only on raw CSS abd JavaScript.

The kit comes in fact with handy front-end development tools and commodities like SASS and Vue.js, already configured with Webpack and integrated with Django static files and templates system using [django-webpack-loader](https://github.com/owais/django-webpack-loader).

## Start up
You need python (>=3.7), npm and node installed on your machine.

Place yourself in your projects folder and clone this repository:
```
git clone https://github.com/loparello/nebula.git
```

## Setup virtual environment
Move to the new created "nebula" folder.
```
cd nebula
```

Here you need to create your virtual environment where the Django project will work and where you will install and keep all your dependancies.
Create the virtual environment directory inside your project with the following comand.

**On Windows**
```
python -m venv venv
```

**On Linux and OS X**
```
python3 -m venv venv
```
```venv``` is the name of the virtual environment directory. You can name it as you want (e.g. ```myvenv```, ```env```, etc.) but stick to lowercase and use no spaces.

Then you need to enter the virtual environment by running:

**On Windows**
```
venv\Scripts\activate
```
**NOTE:** on Windows 10 you might get an error in the Windows PowerShell that says execution of scripts is disabled on this system. In this case, open another Windows PowerShell with the "Run as Administrator" option. Then try typing the following command before starting your virtual environment:
```
C:\WINDOWS\system32> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
Execution Policy Change
The execution policy helps protect you from scripts that you do not trust. Changing the execution policy might expose you to the security risks described in the about_Execution_Policies help topic at http://go.microsoft.com/fwlink/?LinkID=135170. Do you want to change the execution policy? [Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): A
```

**On Linux and OS X**
```
source venv/bin/activate
```

## Install Django
First make sure that you have the latest version of pip, the software that we use to install Django:
```
python -m pip install --upgrade pip
```
Once you have the latest pip version you can install Django with all the preject dependancies by referring a ```requirements.txt``` file in the installation.
**WARNING:** double check to be inside the virtual environment ```(venv)``` before running this command.
```
pip install -r requirements.txt
```

## Setup and update database
Create a new database and name it as you want (suggested "nebuladb").

Then you need to setup an ```.env``` file that will keep your database details and credentials, plus other options. The file will be automatically loaded in the project ```settings.py ``` that will use that the constants you defined.
There is already a file named ```.env.example``` to use as template. Just copy it and rename it ```.env```. Then replace the example values with yours:
```
APP_ENV=local
DEBUG=True
SECRET_KEY=secret-key

DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db
DB_USER=db-user
DB_PASSWORD=secret
DB_HOST=localhost

ALLOWED_HOSTS=host1,host2 
```
**NOTE:** 
- ```DEBUG``` should be set to True if you are in development and to False if you are in production.
- ```SECRET_KEY``` A secret key for a particular Django installation. This is used to provide cryptographic signing, and should be set to a unique, unpredictable value. Generate a random long string with letters, numbers and symbols and replace the default value. Keep it secret, in particular the production one.
- ```DB_ENGINE``` should be set for the database type you want to use (e.g. MYSQL, Postgres, ect...).
- ```ALLOWED_HOSTS``` can be blank in development as this parameter is mostly used in production with your host domain. 

Try to connect and update the database structure by running:
```
python manage.py migrate
```

## Install node.js dependancies
Install all node dependancies for front-end development by running:
```
npm install
```

## Run the project
Start the virtual enrvirnment server by running:
```
python manage.py runserver
```

You can also use the npm script:
```
npm run runserver
```

Then run the front-end tools for compiling and updating JavaScript and Sass with this command:
```
npm run dev
```

The project will run at *localhost:8000*. The first you will load the project you will get an error because there is no page defined in the app "pages". To do so you need to create first a super user to access the admin back-end.

## Create admin super user
In the virtual environment run the following command:
```
python manage.py createsuperuser
```
Answer the questions to define your credentials and your super user account will be created.
Then go to *localhost:8000/admin* to login. Onced logged in go to the "pages" app and add a "home" and an "about" page.


Everything is ready to go now. Enjoy the development!
