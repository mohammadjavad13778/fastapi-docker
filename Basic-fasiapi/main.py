# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Salam Mohammad! Docker + FastAPI is ready."}

