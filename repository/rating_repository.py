from sqlalchemy.orm import Session
from typing import List
from models.ratting import Rating 

class RatingRepository:
    @staticmethod
    def get_all_product_ratings(product_id: int, db: Session) -> List[Rating]:
        return db.query(Rating).filter(Rating.product_id == product_id).all()

    @staticmethod
    def save(rating: Rating, db: Session) -> Rating:
        db.add(rating)
        db.commit()
        db.refresh(rating)
        return rating

    @staticmethod
    def find_by_id(rating_id: int, db: Session) -> Rating:
        return db.query(Rating).filter(Rating.id == rating_id).first()

    @staticmethod
    def add(self, db: Session, rating: Rating):
        db.add(rating)
        db.commit()
        db.refresh(rating)
        return rating

    @staticmethod
    def delete(self, db: Session, rating: Rating):
        db.delete(rating)
        db.commit()

    @staticmethod
    def get_all_product_rating(self, db: Session, product_id: int):
        return db.query(Rating).filter(Rating.product_id == product_id).all()
