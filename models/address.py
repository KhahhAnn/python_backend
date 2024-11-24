from sqlalchemy import Column, String, Integer, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from database import Base
from datetime import date

class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    street_address = Column(Text, nullable=False)
    city = Column(String(255), nullable=False)
    state = Column(String(255), nullable=False)
    zip_code = Column(String(10), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))  # Liên kết với bảng Users
    user = relationship("Users", back_populates="addresses")
    mobile = Column(String(15), nullable=False)
    created_at = Column(Date, default=date.today)
    updated_at = Column(Date, onupdate=date.today)