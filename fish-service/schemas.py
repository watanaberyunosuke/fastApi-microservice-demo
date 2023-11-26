from pydantic import BaseModel


# Complete fish Schema (Pydantic Model)
class Fish(BaseModel):
    fish_id: int
    name: str
    sell: int
    location: str
    difficulty: str
    size: str
    vision: str
    description: str

    class Config:
        from_attributes = True
