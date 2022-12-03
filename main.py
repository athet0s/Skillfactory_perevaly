from fastapi import FastAPI, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from schemas import Pereval
from classes import PerevalManager

app = FastAPI()


@app.exception_handler(RequestValidationError)
def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({"status": 400, "message": "Поля заполненны неверно", "id": None})
    )


@app.post("/submit")
def submitData(data: Pereval):
    try:
        pereval_manager = PerevalManager()
        with pereval_manager as db:
            added_pereval_id = db.insert_data(data)
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=jsonable_encoder({"status": 500, "message": "Ошибка подключения к базе данных", "id": None})
        )
    return {"status": 200, "message": "Отправлено успешно", "id": added_pereval_id}


@app.get("/submitData/{pereval_id}")
def get_pereval(pereval_id: int):
    pereval_manager = PerevalManager()
    with pereval_manager as db:
        pereval_data = db.get_pereval_data_by_id(pereval_id)
    if not pereval_data:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=jsonable_encoder({"status": 404, "message": "Перевал с данным id не найден", "id": pereval_id})
        )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(pereval_data)
    )


@app.get("/submitData")
def get_user_perevals(user_email: str):
    pereval_manager = PerevalManager()
    with pereval_manager as db:
        user_perevals = db.get_perevals_by_user_email(user_email)
    if not user_perevals:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=jsonable_encoder({"status": 404, "message": "Не найденно перевалов от пользовтеля", "id": None})
        )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(user_perevals)
    )

