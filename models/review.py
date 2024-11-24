from sqlalchemy import Column, Float, ForeignKey, Text, DateTime, Integer
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Review(Base):
    __tablename__ = 'review'

    id = Column(Integer, primary_key=True, autoincrement=True)

    review = Column(Text, nullable=True)

    stars_number = Column(Float, nullable=True)

    product_id = Column(ForeignKey('product.id'))
    product = relationship("Product", back_populates="reviews")

    user_id = Column(ForeignKey('users.id'))
    user = relationship("Users", back_populates="reviews")

    created_at = Column(DateTime, default=datetime.utcnow)

    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
