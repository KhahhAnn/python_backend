from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ReviewSchema(BaseModel):
    id: Optional[int]
    review: Optional[str]
    stars_number: Optional[float]
    product_id: Optional[int]
    user_id: Optional[int]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True
        orm_mode = True  # Cho phép chuyển đổi giữa SQLAlchemy model và Pydantic model
