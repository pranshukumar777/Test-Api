from pydantic import BaseModel, Field, EmailStr, validator


class Participant(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(max_length=15)
    contact: str
    email: EmailStr
