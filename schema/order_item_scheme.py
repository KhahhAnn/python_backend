from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Định nghĩa schema cho OrderItem
class OrderItemSchema(BaseModel):
    id: int
    order_id: int
    product_id: int
    size: str
    quantity: int
    price: float
    discounted_price: Optional[float]
    delivery_date: Optional[datetime]

    class Config:
        orm_mode = True
