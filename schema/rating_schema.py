from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class RatingSchema(BaseModel):
    id: Optional[int]
    user_id: int
    product_id: int
    rating: float
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True
        orm_mode = True
