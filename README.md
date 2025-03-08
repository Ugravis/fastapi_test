When you start working on a Python project for the first time, create a virtual environment inside your project: **python -m venv .venv**
Activate the new virtual environment so that any Python command you run or package you install uses it (do it every time): **source .venv/bin/activate**

```
fastapi_test
└─ app
   ├─ __init__.py
   ├─ db
   │  ├─ __init__.py
   │  ├─ database.py
   │  └─ models
   │     ├─ __init__.py
   │     └─ user.py
   ├─ main.py
   └─ routers
      ├─ __init__.py
      └─ users.py
```