from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum


class responselength(str, Enum):
    short = "short"
    long = "long" 

class ContentResponse(BaseModel):
    prompt: str
    content: dict

class ContentRequest(BaseModel):
    review: str
    ratings: int
    length: str
    food_items: str | list[str]
    customer_name: str
    status: str
    type: str
    additional_context:str

class ContentRatings(BaseModel):
    ratings: int
    name: str
