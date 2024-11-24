from pydantic import BaseModel

class Activity(BaseModel):
    id: int
    name: str
    parms_url: str