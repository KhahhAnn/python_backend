from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, autoincrement=True)

    # Tương đương với @Size(max = 50)
    name = Column(String(50), nullable=True)

    # Quan hệ Many-to-One với chính nó (Parent-Child Relationship)
    parent_category_id = Column(Integer, ForeignKey('category.id'), nullable=True)
    parent_category = relationship("Category", remote_side=[id], back_populates="subcategories")

    # Độ sâu của danh mục (level)
    level = Column(Integer, nullable=False)

    # Timestamp cho created_at và updated_at
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Quan hệ với các danh mục con (One-to-Many)
    subcategories = relationship("Category", back_populates="parent_category", cascade="all, delete-orphan")

    def __init__(self, name, parent_category=None, level=0):
        self.name = name
        self.parent_category = parent_category
        self.level = level
