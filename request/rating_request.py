from pydantic import BaseModel

class RatingRequest(BaseModel):
    productId: int
    rating: float