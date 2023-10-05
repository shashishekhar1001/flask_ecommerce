# flask_login_example
Basic Barebone Flask authentication Web App using Flask Login and Auth Blueprint with pages styled using Bulma!

<br />

# Home Page!
http://localhost:5000
[![Home-Page.png](https://i.postimg.cc/hGwh03sh/Home-Page.png)](https://postimg.cc/KKPZGfdy)

<br />

<br />

# Signup page :
http://localhost:5000/auth/signup
[![Sign-Up-Page.png](https://i.postimg.cc/hP35ZJTx/Sign-Up-Page.png)](https://postimg.cc/JGZxGzT4)

<br />

<br />

# Login Page :
http://localhost:5000/auth/login
[![Login-Page.png](https://i.postimg.cc/RV8gQkxL/Login-Page.png)](https://postimg.cc/3dXj3bRk)

<br />

<br />

# Profile Page :
http://localhost:5000/profile
[![Profile-Page.png](https://i.postimg.cc/635VNcNQ/Profile-Page.png)](https://postimg.cc/DWH4rq0V)

<br />




# 👉 Set Up for Windows
Install modules via VENV (windows)
```bash
$ virtualenv env
$ .\env\Scripts\activate
$ pip3 install -r requirements.txt
```
<br />

# 👉 Set Up for Unix, MacOS
Install modules via VENV
```bash
$ virtualenv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```

<br />

# How to run :
Run from one directory above project:-
```bash
$ flask --app project run --debug
```
<br />
At this point, the app runs at http://127.0.0.1:5000/.
<br />


# ✨ Code-base structure:
<br />

```bash
<PROJECT ROOT>:.
|   auth.py
|   main.py
|   models.py
|   requirements.txt
|   __init__.py
|   
+---templates
|   |   base.html
|   |   index.html
|   |   profile.html
|   |   
|   \---auth
|           login.html
|           signup.html
```
<br />

# Note:

Use the correct path to point sqlite db in __init__.py
```bash
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///E:/Flask_Basic_Auth/SRC/db.sqlite'
``` 
<br />
Create SQlite DB using following commands

```bash
$ python
>>> from project import db, create_app, models
>>> app = create_app()
>>> app.app_context().push()
>>> db.create_all()
```
<br />
db.sqlite shall be now created in project root folder