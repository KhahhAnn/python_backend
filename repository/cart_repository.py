from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import Optional
from models.cart import Cart

class CartRepository:
    @staticmethod
    def find_by_user_id(user_id: int, db: Session) -> Optional[Cart]:
        return db.query(Cart).filter(Cart.user_id == user_id).first()
