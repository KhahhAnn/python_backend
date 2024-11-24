from sqlalchemy.orm import Session
from models.orderItem import OrderItem

class OrderItemRepository:
    @staticmethod
    def add(db: Session, order_item: OrderItem) -> OrderItem:
        db.add(order_item)
        db.commit()
        db.refresh(order_item)
        return order_item

    @staticmethod
    def save(order_item: OrderItem, db: Session) -> OrderItem:
        db.add(order_item)
        db.commit()
        db.refresh(order_item)
        return order_item

    @staticmethod
    def find_by_id(order_item_id: int, db: Session) -> OrderItem:
        return db.query(OrderItem).filter(OrderItem.id == order_item_id).first()

    @staticmethod
    def get_all(db: Session):
        return db.query(OrderItem).all()
