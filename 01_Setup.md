#How To Create a Django Web App

## Project Set-Up

1. Install the python packcage `virtualevn` to create a new virtual enviroment
    ```bash
    pip install virtualenv
    ```
2. Create a virtual enviroment
    ```bash
    virutalenv crashblog_env
    ```
3. Activate the virtual enviroment
    ```bash
    source ./crashblog_env/Scripts/activate
    ```
4. Install Django
    ```bash
    pip install django
    ```
5. Create a new project
    ```bash
    django-admin startproject crashblog
    ```
6. Enter to the Django project 
```bash
    ls
    $cd crashblog
```
7. Initilize the DB
```bash
    py manage.py migrate
```
8. One's that we have the DB we can create the superuse
```bash
py manage.py createsuperuser
```
9. Run the development server
```bash
py manage.py runserver
```