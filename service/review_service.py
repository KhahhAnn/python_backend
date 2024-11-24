from fastapi import HTTPException
from sqlalchemy.orm import Session

from exception.product_exception import ProductException
from models.product import Product
from models.review import Review
from models.user import Users
from repository.review_repository import ReviewRepository
from request.review_request import ReviewRequest  # Assuming you have a ReviewRequest model

class ReviewService:
    def __init__(self, db: Session):
        self.db = db
        self.repository = ReviewRepository()

    def create_review(self, req: ReviewRequest, user: Users) -> Review:
        product = self.repository.find_by_id(self.db, req.product_id)  # Fetch product first
        if not product:
            raise ProductException(f"Product not found with id - {req.product_id}")

        review = Review()
        review.review = req.review
        review.stars_number = req.start
        review.user = user
        review.product = product

        return self.repository.add(self.db, review)

    def get_products_review(self, product_id: int) -> List[Review]:
        return self.repository.get_all_product_review(self.db, product_id)

    def delete_review(self, review_id: int):
        self.repository.delete(self.db, review_id)
