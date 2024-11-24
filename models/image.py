from sqlalchemy import Column, String, DateTime, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID as SQLAlchemyUUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from database import Base

class Images(Base):
    __tablename__ = 'images'

    id = Column(SQLAlchemyUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    img_name = Column(String, nullable=True)

    img_data = Column(Text, nullable=True)

    create_at = Column(DateTime(timezone=True), server_default=func.now())

    update_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Many-to-One relationship with Product
    products_id = Column(SQLAlchemyUUID(as_uuid=True), ForeignKey('product.id'))

    product = relationship("Product", back_populates="images")
