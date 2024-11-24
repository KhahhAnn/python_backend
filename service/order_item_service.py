from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.orderItem import OrderItem
from repository.order_item_repository import OrderItemRepository


class OrderItemService:
    def __init__(self, db: Session, repository: OrderItemRepository):
        self.db = db
        self.repository = repository

    def create_order_item(self, order_item: OrderItem) -> OrderItem:
        return self.repository.add(self.db, order_item)
