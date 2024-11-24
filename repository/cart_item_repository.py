from sqlalchemy.orm import Session
from sqlalchemy import select, delete, func
from typing import Optional
from models.cart import Cart
from models.product import Product
from models.cartItem import CartItem



class CartItemRepository:
    @staticmethod
    def is_cart_item_exist(cart: Cart, product: Product, size: str, db: Session) -> Optional[CartItem]:
        return db.query(CartItem).filter(
            CartItem.cart == cart,
            CartItem.product == product,
            CartItem.size == size
        ).first()

    @staticmethod
    def delete_cart_item_by_id(item_id: int, db: Session):
        db.query(CartItem).filter(CartItem.id == item_id).delete()
        db.commit()

    @staticmethod
    def count_cart_items_by_cart_id(cart_id: int, db: Session) -> int:
        return db.query(func.count(CartItem.id)).filter(CartItem.cart_id == cart_id).scalar()
