from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID as SQLAlchemyUUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from database import Base

class ImportInvoiceDetail(Base):
    __tablename__ = 'invoice_detail'

    id = Column(SQLAlchemyUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    quantity_import = Column(Integer, nullable=False)

    total = Column(Float, nullable=False)

    create_at = Column(DateTime(timezone=True), server_default=func.now())

    update_at = Column(DateTime(timezone=True), onupdate=func.now())

    # One-to-One relationship with Product
    product_id = Column(SQLAlchemyUUID(as_uuid=True), ForeignKey('product.id'))
    product = relationship("Product")

    # Many-to-One relationship with ImportInvoice
    import_invoice_id = Column(SQLAlchemyUUID(as_uuid=True), ForeignKey('import_invoice.id'))
    import_invoice = relationship("ImportInvoice", back_populates="import_invoice_details")
