from pydantic import BaseModel
from typing import Optional
from datetime import date

class AddressSchema(BaseModel):
    id: Optional[int]
    first_name: str
    last_name: str
    street_address: str
    city: str
    state: str
    zip_code: str
    user_id: Optional[int]  # Có thể không có khi không cần tham chiếu đến người dùng
    mobile: str
    created_at: Optional[date]  # Kiểu date
    updated_at: Optional[date]  # Kiểu date

    class Config:
        orm_mode = True  # Giúp Pydantic chuyển đổi từ SQLAlchemy model sang schema
        from_attributes = True
