from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel

from schema.order_item_scheme import OrderItemSchema


class OrderSchema(BaseModel):
    id: int
    order_id: str
    user_id: int
    order_items: List[OrderItemSchema]  # Liên kết đến danh sách OrderItem
    order_date: datetime
    delivery_date: Optional[datetime]
    shipping_address_id: int
    total_price: float
    total_discounted_price: Optional[float]
    discount: Optional[float]
    order_status: str
    is_payment: str
    total_item: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True