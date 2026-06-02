from fastapi import FastAPI
from utils import IO
app=FastAPI()
file_path="soldiers.json"



@app.get("/soliders")
def get_soliders():
    return IO.load_soliders_from_jason(file_path)

    