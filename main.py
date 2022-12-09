from fastapi import FastAPI, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List

from schemas import Pereval, PerevalStatusResponse, PerevalResponse, PerevalInfo, PerevalStateResponse
from classes import PerevalManager, PerevalUpdateExeption

app = FastAPI()


@app.exception_handler(RequestValidationError)
def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({"status": 400, "message": "Поля заполненны неверно", "id": None})
    )


@app.post("/submit", response_model=PerevalStatusResponse)
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


@app.get("/submitData/{pereval_id}", response_model=PerevalResponse, responses={404: {"model": PerevalStatusResponse}})
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


@app.get("/submitData", response_model=List[PerevalInfo], responses={404: {"model": PerevalStatusResponse}})
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


@app.patch("/submitData/{pereval_id}", response_model=PerevalStateResponse)
def change_pereval(pereval_id: int, data: Pereval):
    pereval_manager = PerevalManager()
    try:
        with pereval_manager as db:
            db.update_data(pereval_id, data)
    except PerevalUpdateExeption as er:
        error_messages = ["Перевал с указанным id не найден",
                          "Пользователь с указанным email не найден",
                          "Пользователь с указанным email не является авторм записи о перевале с указанным id"]
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=jsonable_encoder({'state': 0, 'message': error_messages[er.error_code]})
        )

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({'state': 1, 'message': 'обновление прошло успешно'})
    )

