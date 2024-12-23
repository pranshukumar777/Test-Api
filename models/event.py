from pydantic import BaseModel, Field
from datetime import date
class Event(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(max_length=15)
    venue:str
    startDate:date
    endDate:date
    description: str = Field(min_length=10)
