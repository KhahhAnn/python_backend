from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Cart(Base):
    __tablename__ = "cart"

    id = Column(Integer, primary_key=True, autoincrement=True)

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship("Users", back_populates="cart")

    cart_item = relationship("CartItem", back_populates="cart", cascade="all, delete-orphan", lazy="joined")

    total_price = Column(Float, nullable=False)
    total_item = Column(Integer, nullable=False)
    total_discounted_price = Column(Float, nullable=True)
    discount = Column(Float, nullable=True)

    def __init__(self, user, total_price=0, total_item=0, total_discounted_price=0, discount=0):
        self.user = user
        self.total_price = total_price
        self.total_item = total_item
        self.total_discounted_price = total_discounted_price
        self.discount = discount
