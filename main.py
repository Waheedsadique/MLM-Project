from fastapi import FastAPI
from db import create_db_and_tables , get_db

app = FastAPI()
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
async def root():
    return {"message": "Hello World"}
