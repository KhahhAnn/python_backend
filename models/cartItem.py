from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class CartItem(Base):
    __tablename__ = "cart_item"

    id = Column(Integer, primary_key=True, autoincrement=True)

    # Quan hệ nhiều-nhiều với Cart
    cart_id = Column(Integer, ForeignKey('cart.id'), nullable=False)
    cart = relationship("Cart", back_populates="cart_item")

    # Quan hệ nhiều-nhiều với Product
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    product = relationship("Product", back_populates="cart_items")

    size = Column(String(10), nullable=True)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    discounted_price = Column(Float, nullable=True)

    def __init__(self, cart, product, size, quantity, price, discounted_price):
        self.cart = cart
        self.product = product
        self.size = size
        self.quantity = quantity
        self.price = price
        self.discounted_price = discounted_price
