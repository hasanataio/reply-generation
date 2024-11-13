from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum


class responselength(str, Enum):
    short = "short"
    long = "long" 

class ContentResponse(BaseModel):
    content: dict

class ContentRequest(BaseModel):
    review: str
    ratings: str
    length: str
    food_items: str | list[str]
    customer_name: str
    additional_context:str
    previous_replies: list[str]

class ContentRatings(BaseModel):
    ratings: int
    name: str



class ContentRequestTesting(BaseModel):
    review: str
    ratings: str
    length: str
    food_items: str | list[str]
    customer_name: str
    additional_context:str
    previous_replies: list[str]
    prompt:str