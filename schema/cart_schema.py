from pydantic import BaseModel
from typing import List, Optional

from schema.cart_item_schema import CartItemSchema


class CartSchema(BaseModel):
    id: int
    user_id: int
    total_price: float
    total_item: int
    total_discounted_price: Optional[float] = None
    discount: Optional[float] = None
    cart_item: List[CartItemSchema]  # Liên kết với các item trong giỏ hàng

    class Config:
        orm_mode = True
        from_attributes = True  # Dùng thuộc tính của SQLAlchemy để ánh xạ với schema

