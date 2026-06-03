from fastapi import FastAPI
from utils import IO
from logger_config import logger
from utils import helper

app=FastAPI()
file_path="soldiers.json"




@app.get("/soldiers")
def get_soliders():
    return IO.load_soliders_from_jason(file_path)


@app.get("/soliders/{id}")
def get_one_soliders(id:int):
    return IO.get_one_solider(file_path,id)


@app.post("/soliders")
def create_solider(body:dict):
    IO.add_solider(file_path,body)
    
@app.put("/soliders/{id}")
def update_soldier(id:int,data:str):
    IO.update_role(file_path,id,data)
    
    
@app.delete("/soliders/{id}")
def delete_solider(id:int):
    IO.remove_solider(file_path,id)
    
