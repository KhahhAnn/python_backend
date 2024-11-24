from sqlalchemy import Column, String, Float, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class Order(Base):
    __tablename__ = 'order_table'

    id = Column(Integer, primary_key=True, autoincrement=True)

    order_id = Column(String, nullable=False, unique=True)

    user_id = Column(ForeignKey('users.id'))
    user = relationship("Users")

    # One-to-Many relationship with OrderItem
    order_items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")

    order_date = Column(DateTime(timezone=True), server_default=func.now())

    delivery_date = Column(DateTime(timezone=True))

    # One-to-One relationship with Address
    shipping_address_id = Column(ForeignKey('address.id'))
    shipping_address = relationship("Address")

    total_price = Column(Float, nullable=False)

    total_discounted_price = Column(Float)

    discount = Column(Float)

    order_status = Column(String, nullable=False)

    is_payment = Column(String, default="Đã thanh toán")

    total_item = Column(Integer, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
