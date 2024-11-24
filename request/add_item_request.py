from pydantic import BaseModel

class AddItemRequest(BaseModel):
    productId: int
    size: str
    quantity: int
    price: float