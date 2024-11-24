from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class CategorySchema(BaseModel):
    id: Optional[int]
    name: Optional[str]
    parent_category_id: Optional[int]
    level: int
    created_at: Optional[datetime]  # Sử dụng kiểu datetime
    updated_at: Optional[datetime]  # Sử dụng kiểu datetime
    subcategories: Optional[List['CategorySchema']]

    class Config:
        orm_mode = True
        from_attributes = True
