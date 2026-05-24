from pydantic import BaseModel

class ExpCreate(BaseModel):
    title:str
    amount:int

class ExpResponse(ExpCreate):
    id:int
    class Config:
        from_attributes=True
