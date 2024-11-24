from sqlalchemy import Column, String, Float, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime
from sqlalchemy.dialects.postgresql import ARRAY

class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, autoincrement=True)

    title = Column(String, nullable=False)

    description = Column(String, nullable=True)

    price = Column(Float, nullable=False)

    discounted_price = Column(Float, nullable=True)

    discount_percent = Column(Float, nullable=True)

    quantity = Column(Integer, nullable=False)

    brand = Column(String, nullable=True)

    color = Column(String, nullable=True)

    # Assuming size is stored as an array of strings
    sizes = Column(ARRAY(String), nullable=True)

    image_url = Column(String, nullable=True)

    # Relationships
    category_id = Column(ForeignKey('category.id'))
    category = relationship("Category")

    imagesProducts = relationship("Images", back_populates="product", cascade="all, delete-orphan")

    ratings = relationship("Rating", back_populates="product", cascade="all, delete-orphan")

    reviews = relationship("Review", back_populates="product", cascade="all, delete-orphan")

    num_ratings = Column(Integer, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)

    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
