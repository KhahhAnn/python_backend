from pydantic import BaseModel

class AddProductRequest(BaseModel):
    title: str
    description: str
    price: float
    discountedPrice: float
    quantity: int
    brand: str
    color: str
    imageUrl: str
    categoryId: int