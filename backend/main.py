from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from sqlalchemy import create_engine
import logging
from sqlalchemy.engine.base import Connection
import pymysql

config = {
    'user' : 'user',
    'password' : 'pass',
    'host' : 'db',
    'port' : 3306,
    'database' : 'database'
}

db_user = config.get('user')
db_pwd = config.get('password')
db_host = config.get('host')
db_port = config.get('port')
db_name = config.get('database')

connection_str = f'mysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'
engine = create_engine(connection_str)
connection = engine.connect()

app = FastAPI()

@app.get("/")
def root():
    return "Service is running..."

@app.get("/calculator")
async def calcul(lvlActuel:int=Form(...), lvlVise:int=Form(...),xpActuelle:int=Form(...)):
    return "Calculateur"