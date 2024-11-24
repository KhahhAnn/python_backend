from sqlalchemy import Column, String, DateTime, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID as SQLAlchemyUUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from database import Base

class ImportInvoice(Base):
    __tablename__ = 'import_invoice'

    id = Column(SQLAlchemyUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    invoice_name = Column(String, nullable=True)

    import_date = Column(DateTime, nullable=False)

    total_price = Column(Float, nullable=False)

    create_at = Column(DateTime(timezone=True), server_default=func.now())

    update_at = Column(DateTime(timezone=True), onupdate=func.now())

    # One-to-Many relationship with ImportInvoiceDetail
    import_invoice_details = relationship("ImportInvoiceDetail", back_populates="import_invoice")
