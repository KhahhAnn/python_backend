from datetime import date
import random
from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.address import Address
from models.order import Order
from models.orderItem import OrderItem
from models.user import Users
from repository.order_repository import OrderRepository
from utils.order_status import OrderStatus


class OrderService:
    def __init__(self, db: Session):
        self.db = db
        self.repository = OrderRepository()

    def create_order(self, user: Users, shipping_address: Address) -> Order:
        shipping_address.user = user
        self.db.add(shipping_address)
        self.db.commit()

        user.address_list.append(shipping_address)
        self.db.commit()

        cart = self.repository.get_user_orders(user.id)  # Implement this to get cart from DB
        order = Order(user=user, shipping_address=shipping_address, order_id=str(random.randint(1000, 20000)))

        for item in cart.cart_items:  # Assuming cart has a `cart_items` attribute
            order_item = OrderItem(price=item.price, product=item.product, quantity=item.quantity,
                                   size=item.size, discounted_price=item.discounted_price)
            order.order_items.append(order_item)

        order.total_item = cart.total_item
        order.total_discounted_price = cart.total_discounted_price
        order.created_at = date.today()  # Use date.today() for the current date
        order.order_date = date.today()
        order.order_status = OrderStatus.CHUA_XAC_NHAN_DON

        return self.repository.add(self.db, order)

    def find_order_by_id(self, order_id: int) -> Order:
        order = self.repository.find_by_id(self.db, order_id)
        if not order:
            raise HTTPException(status_code=404, detail="Order not found")
        return order

    def user_order_history(self, user_id: int):
        return self.repository.get_user_orders(self.db, user_id)

    def update_order(self, order: Order):
        existing_order = self.repository.find_by_id(self.db, order.id)
        if not existing_order:
            raise HTTPException(status_code=404, detail="Order not found")

        existing_order.order_status = order.order_status
        existing_order.is_payment = order.is_payment  # Assuming is_payment is part of the Order model
        return self.repository.update(self.db, existing_order)

    def delete_order(self, order_id: int):
        self.repository.delete(self.db, order_id)

    def get_all_orders(self):
        return self.repository.get_all(self.db)
