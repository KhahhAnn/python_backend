from fastapi import HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from uuid import UUID

from models.importInvoiceDetail import ImportInvoiceDetail
from repository.import_invoice_detail_repository import ImportInvoiceDetailRepository


class ImportInvoiceDetailService:
    def __init__(self, db: Session, repository: ImportInvoiceDetailRepository):
        self.db = db
        self.repository = repository

    def add_new_invoice_detail(self, invoice_detail: ImportInvoiceDetail) -> ImportInvoiceDetail:
        new_invoice_detail = ImportInvoiceDetail(**invoice_detail.dict(), create_at=datetime.now(),
                                                 update_at=datetime.now())
        return self.repository.add(self.db, new_invoice_detail)

    def update_invoice_detail(self, id: UUID, invoice_detail: ImportInvoiceDetail) -> ImportInvoiceDetail:
        existing_detail = self.repository.get(self.db, id)
        if not existing_detail:
            raise HTTPException(status_code=404, detail="Invoice detail not found")

        for key, value in invoice_detail.dict(exclude_unset=True).items():
            setattr(existing_detail, key, value)

        existing_detail.update_at = datetime.now()
        return self.repository.update(self.db, existing_detail)

    def delete_invoice_detail(self, id: UUID):
        existing_detail = self.repository.get(self.db, id)
        if not existing_detail:
            raise HTTPException(status_code=404, detail="Invoice detail not found")

        self.repository.delete(self.db, existing_detail)
        return {"message": "Delete complete!"}
