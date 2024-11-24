from pydantic import BaseModel
from typing import Optional, List
from datetime import date, datetime
import uuid

from schema.user_schema import UserSchema


class DiscountSchema(BaseModel):
    id: Optional[uuid.UUID]
    discount_name: str
    percent_discount: float
    apply_date: date
    expiry: date
    create_at: Optional[datetime]  # Thời gian tạo
    update_at: Optional[datetime]  # Thời gian cập nhật
    users_list: Optional[List[UserSchema]]

    class Config:
        from_attributes = True
        orm_mode = True  # Để sử dụng ORM model
