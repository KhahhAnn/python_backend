from datetime import date
from fastapi import HTTPException
from sqlalchemy.orm import Session

from exception.product_exception import ProductException
from models.ratting import Rating
from models.user import Users
from repository.rating_repository import RatingRepository
from request.rating_request import RatingRequest


class RatingService:
    def __init__(self, db: Session):
        self.db = db
        self.repository = RatingRepository()

    def create_rating(self, req: RatingRequest, user: Users) -> Rating:
        product = self.repository.find_by_id(self.db, req.product_id)  # Fetch product first
        if not product:
            raise ProductException(f"Product not found with id - {req.product_id}")

        rating = Rating()
        rating.rating = req.rating
        rating.user = user
        rating.product = product
        rating.created_at = date.today()

        return self.repository.add(self.db, rating)

    def get_products_rating(self, product_id: int) -> List[Rating]:
        return self.repository.get_all_product_rating(self.db, product_id)

    def update_rating(self, rating_id: int, req: RatingRequest, user: Users) -> Rating:
        rating = self.repository.find_by_id(self.db, rating_id)
        if not rating:
            raise RatingException(f"Rating not found with id - {rating_id}")

        if rating.user != user:
            raise HTTPException(status_code=403, detail="Not authorized to update this rating")

        rating.rating = req.rating
        return self.repository.add(self.db, rating)

    def delete_rating(self, rating_id: int, user: Users):
        rating = self.repository.find_by_id(self.db, rating_id)
        if not rating:
            raise RatingException(f"Rating not found with id - {rating_id}")

        if rating.user != user:
            raise HTTPException(status_code=403, detail="Not authorized to delete this rating")

        self.repository.delete(self.db, rating)
