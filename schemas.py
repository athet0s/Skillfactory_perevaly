from typing import List
from pydantic import BaseModel


class User(BaseModel):
    email: str
    phone: str
    name: str
    fam: str
    otc: str


class Image(BaseModel):
    title: str
    base64: str


class Level(BaseModel):
    winter: str
    summer: str
    autumn: str
    spring: str


class Coords(BaseModel):
    height: int
    latitude: float
    longitude: float


class Pereval(BaseModel):
    title: str
    beauty_title: str
    other_titles: str
    add_time: str
    connect: str
    user: User
    images: List[Image]



