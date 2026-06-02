from fastapi import FastAPI


app=FastAPI()


@app.get("/soliders")
def get_soliders():
    pass