from pydantic import BaseModel
from typing import List
from models.cart import Cart
from models.cartItem import CartItem


class CartResponse(BaseModel):
    cart: Cart
    cartItems: List[CartItem]