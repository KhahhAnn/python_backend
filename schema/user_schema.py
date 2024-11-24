from pydantic import BaseModel
from typing import Optional, List
from datetime import date, datetime
from schema.address_schema import AddressSchema
from schema.rating_schema import RatingSchema
from schema.review_schema import ReviewSchema
from schema.role_schema import RoleSchema


class UserSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    password: str
    email: str
    mobile: str
    is_active: bool
    active_code: str
    image_src: Optional[str] = None  # Nếu không có ảnh thì không bắt buộc
    created_at: date
    updated_at: Optional[date]
    addressList: List[AddressSchema] = []  # Liên kết với Address
    ratingList: List[RatingSchema] = []  # Liên kết với Rating
    reviewList: List[ReviewSchema] = []  # Liên kết với Review
    rolesList: List[RoleSchema] = []  # Liên kết với Role

    class Config:
        from_attributes = True
        orm_mode = True  # Để sử dụng ORM model, giúp chuyển đổi từ SQLAlchemy model sang Pydantic model