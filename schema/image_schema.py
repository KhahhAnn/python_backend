from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime

class ImageSchema(BaseModel):
    id: UUID = Field(..., description="ID của ảnh")
    img_name: Optional[str] = Field(None, description="Tên của ảnh")
    img_data: Optional[str] = Field(None, description="Dữ liệu ảnh (có thể là base64 string)")
    create_at: datetime = Field(..., description="Thời gian tạo ảnh")
    update_at: Optional[datetime] = Field(None, description="Thời gian cập nhật ảnh")
    product_id: UUID = Field(..., description="ID của sản phẩm liên kết với ảnh")

    class Config:
        orm_mode = True
