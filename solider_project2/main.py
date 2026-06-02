from fastapi import FastAPI
from utils import IO
from logger_config import logger

app=FastAPI()
file_path="soldiers.json"




@app.get("/soldiers")
def get_soliders():
    return IO.load_soliders_from_jason(file_path)


# @app.get("/soliders")
# def get_soliders():
#     return IO.load_soliders_from_jason(file_path)


@app.post("/soliders")
def create_solider(body:dict):
    IO.add_solider(file_path,body)
    