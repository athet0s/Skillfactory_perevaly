from typing import List
from pydantic import BaseModel, Field


class User(BaseModel):
    email: str = Field(min_length=1)
    phone: str = Field(min_length=1)
    name: str = Field(min_length=1)
    fam: str = Field(min_length=1)
    otc: str = Field(min_length=1)


class Image(BaseModel):
    title: str
    data: str


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



