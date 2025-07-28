from fastapi import APIRouter
from ..schemas import Cocktail
from typing import List

router = APIRouter()


@router.get("/", response_model=List[Cocktail], tags=["Cocktails"])
async def get_cocktails():
    # This is the temporary implementation.
    """
    Retrieve a list of cocktails.
    """
    # Placeholder for actual data retrieval logic
    return [
        Cocktail(name="Mojito", ingredients=["Rum", "Mint", "Lime", "Sugar", "Soda"]),
        Cocktail(name="Margarita", ingredients=["Tequila", "Lime Juice", "Triple Sec"]),
        Cocktail(name="Old Fashioned", ingredients=["Bourbon", "Sugar", "Bitters", "Orange Peel"]),
    ]
