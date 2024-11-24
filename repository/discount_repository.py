from sqlalchemy.orm import Session
from uuid import UUID
from typing import List
from models.discount import Discount

class DiscountRepository:
    @staticmethod
    def save(discount: Discount, db: Session) -> Discount:
        db.add(discount)
        db.commit()
        db.refresh(discount)
        return discount

    @staticmethod
    def find_by_id(discount_id: UUID, db: Session) -> Discount:
        return db.query(Discount).filter(Discount.id == discount_id).first()

    @staticmethod
    def get_all(db: Session) -> List[Discount]:
        return db.query(Discount).all()
