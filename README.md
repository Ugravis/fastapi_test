When you start working on a Python project for the first time, create a virtual environment inside your project: **python -m venv .venv**
Activate the new virtual environment so that any Python command you run or package you install uses it (do it every time): **source .venv/bin/activate**
Default starting command (**fastapi dev app/main.py**) is depreciated -> please use commands specify in the Makefile (for the use of ENVIRONMENT variable). 

```
fastapi_test
└─ app
   ├─ __init__.py
   ├─ api
   │  ├─ __init__.py
   │  └─ api_v1
   │     ├─ __init__.py
   │     ├─ api.py
   │     └─ routes
   │        ├─ __init__.py
   │        └─ users.py
   ├─ config
   │  ├─ __init__.py
   │  └─ config.py
   ├─ db
   │  ├─ __init__.py
   │  ├─ database.py
   │  └─ models
   │     ├─ User.py
   │     └─ __init__.py
   ├─ dependencies
   │  └─ db.py
   ├─ main.py
   ├─ middlewares
   │  └─ log_middleware.py
   ├─ schemas
   │  ├─ __init__.py
   │  └─ user.py
   └─ services
      ├─ __init__.py
      └─ user_service.py

```