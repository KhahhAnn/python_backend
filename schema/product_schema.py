from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

from schema.image_schema import ImageSchema


class ProductSchema(BaseModel):
    id: int = Field(..., description="ID của sản phẩm")
    title: str = Field(..., description="Tên sản phẩm")
    description: Optional[str] = Field(None, description="Mô tả sản phẩm")
    price: float = Field(..., description="Giá sản phẩm")
    discounted_price: Optional[float] = Field(None, description="Giá sau khi giảm")
    discount_percent: Optional[float] = Field(None, description="Phần trăm giảm giá")
    quantity: int = Field(..., description="Số lượng sản phẩm")
    brand: Optional[str] = Field(None, description="Thương hiệu sản phẩm")
    color: Optional[str] = Field(None, description="Màu sắc sản phẩm")
    sizes: Optional[List[str]] = Field(None, description="Danh sách kích thước của sản phẩm")
    image_url: Optional[str] = Field(None, description="URL hình ảnh đại diện sản phẩm")
    category_id: Optional[int] = Field(None, description="ID của danh mục sản phẩm")
    num_ratings: Optional[int] = Field(None, description="Số lượng đánh giá sản phẩm")
    created_at: datetime = Field(..., description="Thời gian tạo sản phẩm")
    updated_at: datetime = Field(..., description="Thời gian cập nhật sản phẩm")
    images: Optional[List[ImageSchema]] = Field(None, description="Danh sách ảnh liên kết với sản phẩm")

    class Config:
        orm_mode = True
