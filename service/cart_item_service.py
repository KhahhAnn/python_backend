from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.cart import Cart
from models.cartItem import CartItem
from repository.cart_item_repository import CartItemRepository
from repository.cart_repository import CartRepository


class CartItemService:
    def __init__(
            self,
            cart_item_repository: CartItemRepository = Depends(),
            cart_repository: CartRepository = Depends(),
            db: Session = Depends(get_db)
    ):
        self.cart_item_repository = cart_item_repository
        self.cart_repository = cart_repository
        self.db = db

    def create_cart_item(self, cart_item: CartItem) -> CartItem:
        new_cart_item = CartItem(
            quantity=1,
            product_id=cart_item.product_id,
            cart_id=cart_item.cart_id
        )
        new_cart_item.price = new_cart_item.product.price * new_cart_item.quantity
        new_cart_item.discounted_price = new_cart_item.product.discounted_price * new_cart_item.quantity
        self.db.add(new_cart_item)
        self.db.commit()
        self.db.refresh(new_cart_item)
        return new_cart_item

    def update_cart_item(self, user_id: int, cart_item_id: int, cart_item: CartItem) -> CartItem:
        item = self.find_cart_item_by_id(cart_item_id)
        if not item:
            raise HTTPException(status_code=404, detail="Cart item not found")

        item.quantity = cart_item.quantity
        item.price = item.quantity * item.product.price
        item.discounted_price = item.quantity * item.product.discounted_price
        self.update_cart_totals(item.cart)

        self.db.commit()
        self.db.refresh(item)
        return item

    def is_cart_item_exist(self, cart_id: int, product_id: int, size: str) -> CartItem:
        return self.cart_item_repository.is_cart_item_exist(cart_id, product_id, size)

    def remove_cart_item(self, cart_item_id: int):
        cart_item = self.find_cart_item_by_id(cart_item_id)
        if not cart_item:
            raise HTTPException(status_code=404, detail="CartItem not found")

        cart = cart_item.cart
        self.db.delete(cart_item)
        self.db.commit()
        self.update_cart_totals(cart)

    def find_cart_item_by_id(self, cart_item_id: int) -> CartItem:
        cart_item = self.db.query(CartItem).filter(CartItem.id == cart_item_id).first()
        if not cart_item:
            raise HTTPException(status_code=404, detail="CartItem not found")
        return cart_item

    def update_cart_totals(self, cart: Cart):
        total_price = sum(item.quantity * item.product.price for item in cart.cart_items)
        total_discounted_price = sum(item.discounted_price for item in cart.cart_items)
        total_items = sum(item.quantity for item in cart.cart_items)
        discount = total_price - total_discounted_price

        cart.total_price = total_price
        cart.total_discounted_price = total_discounted_price
        cart.total_item = total_items
        cart.discount = discount

        self.db.commit()
        self.db.refresh(cart)
