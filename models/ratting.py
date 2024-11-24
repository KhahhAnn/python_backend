from sqlalchemy import Column, Float, ForeignKey, DateTime, Integer
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Rating(Base):
    __tablename__ = 'rating'

    id = Column(Integer, primary_key=True, autoincrement=True)

    user_id = Column(ForeignKey('users.id'), nullable=False)
    user = relationship("Users")

    product_id = Column(ForeignKey('product.id'), nullable=False)
    product = relationship("Product")

    rating = Column(Float, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
