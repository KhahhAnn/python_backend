from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List
from models.review import Review

class ReviewRepository:
    @staticmethod
    def get_all_product_reviews(product_id: int, db: Session) -> List[Review]:
        return db.query(Review).filter(Review.product_id == product_id).all()

    @staticmethod
    def save(review: Review, db: Session) -> Review:
        db.add(review)
        db.commit()
        db.refresh(review)
        return review

    @staticmethod
    def find_by_id(review_id: int, db: Session) -> Review:
        return db.query(Review).filter(Review.id == review_id).first()

    @staticmethod
    def add(self, db: Session, review: Review):
        db.add(review)
        db.commit()
        db.refresh(review)
        return review

    @staticmethod
    def get_all_product_review(self, db: Session, product_id: int):
        return db.query(Review).filter(Review.product_id == product_id).all()

    @staticmethod
    def delete(self, db: Session, review_id: int):
        review = self.find_by_id(db, review_id)
        if review:
            db.delete(review)
            db.commit()
        else:
            raise Exception("Review not found")
