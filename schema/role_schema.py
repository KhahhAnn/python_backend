from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class RoleSchema(BaseModel):
    id: Optional[str]
    role_name: str
    create_at: Optional[datetime]
    update_at: Optional[datetime]
    user_list: Optional[List['UserSchema']]  # Danh sách người dùng liên kết với vai trò này

    class Config:
        from_attributes = True
        orm_mode = True  # Cho phép chuyển đổi giữa SQLAlchemy model và Pydantic model
