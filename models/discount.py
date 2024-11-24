from sqlalchemy import Column, String, Float, Date, Table, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID as SQLAlchemyUUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from database import Base

# Bảng liên kết giữa Discount và Users (Many-to-Many relationship)
user_discount = Table(
    'user_discount',
    Base.metadata,
    Column('discount_id', SQLAlchemyUUID(as_uuid=True), ForeignKey('discount.id')),
    Column('user_id', ForeignKey('users.id'))
)

class Discount(Base):
    __tablename__ = 'discount'

    id = Column(SQLAlchemyUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    discount_name = Column(String, nullable=False)

    percent_discount = Column(Float, nullable=False)

    apply_date = Column(Date, nullable=False)

    expiry = Column(Date, nullable=False)

    create_at = Column(DateTime(timezone=True), server_default=func.now())

    update_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Many-to-Many relationship với Users
    users_list = relationship("Users", secondary=user_discount, back_populates="discounts")
