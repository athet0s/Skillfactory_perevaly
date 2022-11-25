from fastapi import FastAPI

from schemas import Pereval
from classes import PerevalManager

app = FastAPI()

@app.post("/submit")
def submitData(data: Pereval):
    result = {"status": 200, "message": "Отправлено успешно", "id": None}
    print(data)
    return result