from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID as SQLAlchemyUUID
from sqlalchemy.sql import func
import uuid
from database import Base

class Event(Base):
    __tablename__ = 'event'

    id = Column(SQLAlchemyUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    event_name = Column(String, nullable=False)

    image = Column(Text)

    link = Column(Text)

    create_at = Column(DateTime(timezone=True), server_default=func.now())

    update_at = Column(DateTime(timezone=True), onupdate=func.now())
