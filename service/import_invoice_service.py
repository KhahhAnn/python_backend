from uuid import UUID

from fastapi import HTTPException
from sqlalchemy.orm import Session
from datetime import datetime  # Import datetime

from models.importInvoice import ImportInvoice
from repository.import_invoice_repository import ImportInvoiceRepository


class ImportInvoiceService:
    def __init__(self, db: Session, repository: ImportInvoiceRepository):
        self.db = db
        self.repository = repository

    def add_new_invoice(self, import_invoice: ImportInvoice) -> ImportInvoice:
        new_invoice = ImportInvoice(
            import_date=import_invoice.import_date or datetime.now().date(),
            invoice_name=import_invoice.invoice_name,
            total_price=import_invoice.total_price,
            import_invoice_details=import_invoice.import_invoice_details,
            create_at=datetime.now(),
            update_at=datetime.now()
        )
        return self.repository.add(self.db, new_invoice)

    def update_invoice(self, id: UUID, import_invoice: ImportInvoice) -> ImportInvoice:
        existing_invoice = self.repository.get(self.db, id)
        if not existing_invoice:
            raise HTTPException(status_code=404, detail="Invoice not found")

        # Update fields, only change if provided
        existing_invoice.import_date = import_invoice.import_date or existing_invoice.import_date
        existing_invoice.invoice_name = import_invoice.invoice_name or existing_invoice.invoice_name
        existing_invoice.total_price = import_invoice.total_price if import_invoice.total_price > 0 else existing_invoice.total_price
        existing_invoice.import_invoice_details = import_invoice.import_invoice_details or existing_invoice.import_invoice_details
        existing_invoice.update_at = datetime.now()

        return self.repository.update(self.db, existing_invoice)

    def delete_invoice(self, id: UUID):
        existing_invoice = self.repository.get(self.db, id)
        if not existing_invoice:
            raise HTTPException(status_code=404, detail="Invoice not found")

        self.repository.delete(self.db, existing_invoice)
        return {"message": "Delete complete!"}
