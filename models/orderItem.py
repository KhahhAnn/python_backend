from sqlalchemy import Column, String, Float, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class OrderItem(Base):
    __tablename__ = 'order_item'

    id = Column(Integer, primary_key=True, autoincrement=True)

    # Many-to-One relationship with Order
    order_id = Column(ForeignKey('order_table.id'))
    order = relationship("Order", back_populates="order_items")

    # Many-to-One relationship with Product
    product_id = Column(ForeignKey('product.id'))
    product = relationship("Product")

    size = Column(String)

    quantity = Column(Integer, nullable=False)

    price = Column(Float, nullable=False)

    discounted_price = Column(Float)

    delivery_date = Column(DateTime(timezone=True))
