from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import DatabaseHandler as db
import logging

app = FastAPI()

@app.get("/")
def root():
    logging.info("a")
    return "Service is running..."

@app.get("/calculator")
async def calcul():
    return "Calculateur"

@app.get("/jobs")
async def jobs():
    return "jobs"

@app.get("/jobs/{jobid}")
async def job(jobid: int):
    return db.GetCraftByJobId(jobid)