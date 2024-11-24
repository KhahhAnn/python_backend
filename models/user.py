from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Date, Table, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base
from datetime import date

# Bảng trung gian để liên kết users và roles.py
users_roles = Table(
    'users_roles', Base.metadata,
    Column('id_user', Integer, ForeignKey('user.id')),
    Column('id_role', Integer, ForeignKey('roles.py.id'))
)

class Users(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    mobile = Column(String(15), nullable=False)

    is_active = Column(Boolean, nullable=False, default=True)
    active_code = Column(String(255), nullable=False)

    # Quan hệ một-nhiều với Address, Rating, và Review
    addressList = relationship("Address", back_populates="user", cascade="all, delete-orphan")
    reatingList = relationship("Rating", back_populates="user", cascade="all, delete-orphan")
    reviewList = relationship("Review", back_populates="user", cascade="all, delete-orphan")

    # Quan hệ nhiều-nhiều với Roles
    rolesList = relationship("Roles", secondary=users_roles, back_populates="users", lazy="joined")

    image_src = Column(Text, nullable=True)

    created_at = Column(Date, server_default=func.now())  # Tương đương với @CreationTimestamp
    updated_at = Column(Date, onupdate=func.now())  # Tương đương với @UpdateTimestamp
