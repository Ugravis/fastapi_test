from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return { "message": "Hello world from FastAPI" }

@app.get('/users/me')
async def read_user_me():
    return { "user_id": "it's me Mario" }

@app.get('/users/{user_id}')
async def read_user(user_id: int):
    return { "user_id": user_id }