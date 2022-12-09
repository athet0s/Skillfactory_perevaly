from typing import List, Union
from pydantic import BaseModel, Field


class User(BaseModel):
    email: str = Field(min_length=1)
    phone: str = Field(min_length=1)
    name: str = Field(min_length=1)
    fam: str = Field(min_length=1)
    otc: str = Field(min_length=1)


class Image(BaseModel):
    title: str = Field(min_length=1)
    data: str = Field(min_length=1)


class Level(BaseModel):
    winter: str
    summer: str
    autumn: str
    spring: str


class Coords(BaseModel):
    height: str = Field(min_length=1)
    latitude: str = Field(min_length=1)
    longitude: str = Field(min_length=1)


class Pereval(BaseModel):
    title: str = Field(min_length=1)
    beauty_title: str
    other_titles: str
    add_time: str
    connect: str
    user: User
    images: List[Image]
    coords: Coords
    level: Level


class PerevalStatusResponse(BaseModel):
    status: int = 200
    message: str
    id: Union[int, None] = None


class PerevalResponse(BaseModel):
    id: int
    date_added: str
    status: str
    beauty_title: str
    title: str
    other_titles: str
    connect: str
    add_time: str
    level_winter: str
    level_summer: str
    level_autumn: str
    level_spring: str
    latitude: float
    longitude: float
    height: int


class PerevalInfo(BaseModel):
    id: int
    title: str
    beauty_title: str
    status: str
    date_added: str
    latitude: float
    longitude: float
    height: float


class PerevalStateResponse(BaseModel):
    state: int
    message: str
