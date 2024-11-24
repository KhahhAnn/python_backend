from pydantic import BaseModel
from typing import Set

from models.size import Size


class CreateProductRequest(BaseModel):
    title: str
    description: str
    price: float
    discountedPrice: float
    discountPercent: float
    quantity: int
    brand: str
    color: str
    size: Set[Size] = set()
    imageUrl: str
    topLevelCategory: str
    secondLevelCategory: str
    thirdLevelCategory: str