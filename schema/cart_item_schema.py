from pydantic import BaseModel
from typing import Optional

class CartItemSchema(BaseModel):
    id: int
    cart_id: int
    product_id: int
    size: Optional[str] = None  # Có thể là null nếu không có kích thước
    quantity: int
    price: float
    discounted_price: Optional[float] = None

    class Config:
        orm_mode = True  # Giúp chuyển đổi từ SQLAlchemy model sang Pydantic schema
        from_attributes = True  # Dùng thuộc tính của SQLAlchemy để ánh xạ với schema

