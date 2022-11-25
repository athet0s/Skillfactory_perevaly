from fastapi import FastAPI

from schemas import Pereval
from classes import PerevalManager

app = FastAPI()


@app.post("/submit")
def submitData(data: Pereval):
    pereval_manager = PerevalManager(data)
    with pereval_manager as db:
        p_id = db.insert_data()
    result = {"status": 200, "message": "Отправлено успешно", "id": p_id}
    return result
