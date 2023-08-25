from fastapi import FastAPI, Depends, HTTPException
from .database import db as connection
from .models import User

from routers import users
app = FastAPI()

app.include_router(users.router)



# Eventos en FastApi
@app.on_event('startup')
def startup():
    if connection.is_closed():
        print('Iniciando BD')
        connection.connect()
    connection.create_tables([User])
@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()


@app.get('/')
async def home():
    return {"message":"Hello world"}


