from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
from database import Base
from uuid import uuid4
from datetime import datetime

class Role(Base):
    __tablename__ = 'roles'

    id = Column(String, primary_key=True, default=str(uuid4()))

    role_name = Column(String(10), nullable=False)

    user_list = relationship("User", secondary="users_roles", back_populates="roles")

    create_at = Column(DateTime, default=datetime.utcnow)

    update_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
