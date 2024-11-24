from pydantic import BaseModel

class ReviewRequest(BaseModel):
    productId: int
    review: str
    start: float