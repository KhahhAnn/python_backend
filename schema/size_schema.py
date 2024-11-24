from pydantic import BaseModel

class SizeSchema(BaseModel):
    id: int
    name: str
    quantity: int

    class Config:
        from_attributes = True
        orm_mode = True  # Cho phép chuyển đổi giữa SQLAlchemy model và Pydantic model
