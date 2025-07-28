from pydantic import BaseModel


class Cocktail(BaseModel):
    id: int
    name: str
    instructions: str
    image_url: str
