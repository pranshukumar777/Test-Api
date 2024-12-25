from typing import Annotated
from pydantic import BaseModel, Field, AfterValidator
from datetime import date, datetime


def isValidStartDate(value):
    if value < datetime.today().date():
        raise ValueError(f"Date is invalid (Past date given : {value}) !!")
    return value


class Event(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(max_length=15)
    venue: str
    startDate: Annotated[date, AfterValidator(isValidStartDate)]
    endDate: Annotated[date, AfterValidator(isValidStartDate)]
    description: str = Field(min_length=10)
