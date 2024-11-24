from sqlalchemy.orm import Session
from typing import List
from models.order import Order 

class OrderRepository:
    @staticmethod
    def add(db: Session, order: Order) -> Order:
        db.add(order)
        db.commit()
        db.refresh(order)
        return order

    @staticmethod
    def find_by_id(db: Session, order_id: int) -> Order:
        return db.query(Order).filter(Order.id == order_id).first()

    @staticmethod
    def get_user_orders(db: Session, user_id: int):
        return db.query(Order).filter(Order.user_id == user_id).all()

    @staticmethod
    def delete(db: Session, order_id: int):
        order = db.query(Order).filter(Order.id == order_id).first()
        if order:
            db.delete(order)
            db.commit()

    @staticmethod
    def get_all(db: Session):
        return db.query(Order).all()

    @staticmethod
    def update(db: Session, order: Order):
        db.merge(order)
        db.commit()
        db.refresh(order)
        return order

    @staticmethod
    def save(order: Order, db: Session) -> Order:
        db.add(order)
        db.commit()
        db.refresh(order)
        return order
