from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from typing import List
from math import ceil

from models.cart import Cart
from models.cartItem import CartItem
from models.user import Users
from repository.cart_item_repository import CartItemRepository
from repository.cart_repository import CartRepository
from repository.product_repository import ProductRepository
from repository.user_repository import UserRepository
from request.add_item_request import AddItemRequest
from response.cart_response import CartResponse


class CartService:
    def __init__(
        self,
        cart_repository: CartRepository = Depends(),
        cart_item_repository: CartItemRepository = Depends(),
        product_repository: ProductRepository = Depends(),
        user_repository: UserRepository = Depends(),
        db: Session = Depends(get_db),
    ):
        self.cart_repository = cart_repository
        self.cart_item_repository = cart_item_repository
        self.product_repository = product_repository
        self.user_repository = user_repository
        self.db = db

    def create_cart(self, user: Users) -> Cart:
        cart = Cart(user_id=user.id)
        self.db.add(cart)
        self.db.commit()
        self.db.refresh(cart)
        return cart

    def add_cart_item(self, user_id: int, req: AddItemRequest) -> str:
        cart = self.cart_repository.find_by_user_id(user_id) or self.create_cart(self.user_repository.find_user_by_id(user_id))

        product = self.product_repository.find_product_by_id(req.product_id)
        existing_cart_item = self.cart_item_repository.is_cart_item_exist(cart.id, product.id, req.size)

        if not existing_cart_item:
            cart_item = CartItem(
                product_id=product.id,
                cart_id=cart.id,
                quantity=req.quantity,
                size=req.size,
                price=req.quantity * product.discounted_price,
            )
            self.db.add(cart_item)
            self.db.commit()
            self.db.refresh(cart_item)
            cart.cart_items.append(cart_item)
        else:
            existing_cart_item.quantity += req.quantity
            existing_cart_item.price = existing_cart_item.quantity * product.discounted_price
            self.db.commit()

        self.update_cart_totals(cart.id)
        return "Item added to cart"

    def find_user_cart(self, user_id: int, page: int = 1, page_size: int = 10) -> CartResponse:
        cart = self.cart_repository.find_by_user_id(user_id)
        if not cart:
            raise HTTPException(status_code=404, detail="Cart not found for user")

        total_items = len(cart.cart_items)
        total_pages = ceil(total_items / page_size)
        start = (page - 1) * page_size
        end = start + page_size
        paginated_items = cart.cart_items[start:end]

        return CartResponse(
            cart=cart,
            cart_items=paginated_items,
            total_items=total_items,
            page=page,
            page_size=page_size,
            total_pages=total_pages
        )

    def count_cart_items(self, user_id: int) -> int:
        cart = self.cart_repository.find_by_user_id(user_id)
        return len(cart.cart_items) if cart else 0

    def update_cart_totals(self, cart_id: int):
        cart = self.cart_repository.find_by_id(cart_id)
        total_price = sum(item.quantity * item.product.price for item in cart.cart_items)
        total_discounted_price = sum(item.price for item in cart.cart_items)
        total_items = sum(item.quantity for item in cart.cart_items)
        discount = total_price - total_discounted_price

        cart.total_price = total_price
        cart.total_discounted_price = total_discounted_price
        cart.total_item = total_items
        cart.discount = discount

        self.db.commit()
        self.db.refresh(cart)
