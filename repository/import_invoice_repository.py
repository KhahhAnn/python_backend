from sqlalchemy.orm import Session
from uuid import UUID
from typing import List
from models.importInvoice import ImportInvoice 

class ImportInvoiceRepository:

    @staticmethod
    def add(db: Session, invoice: ImportInvoice) -> ImportInvoice:
        db.add(invoice)
        db.commit()
        db.refresh(invoice)
        return invoice

    @staticmethod
    def get(db: Session, id: UUID) -> ImportInvoice:
        return db.query(ImportInvoice).filter(ImportInvoice.id == id).first()

    @staticmethod
    def update(db: Session, invoice: ImportInvoice) -> ImportInvoice:
        db.commit()
        db.refresh(invoice)
        return invoice

    @staticmethod
    def delete(db: Session, invoice: ImportInvoice):
        db.delete(invoice)
        db.commit()

    @staticmethod
    def save(import_invoice: ImportInvoice, db: Session) -> ImportInvoice:
        db.add(import_invoice)
        db.commit()
        db.refresh(import_invoice)
        return import_invoice

    @staticmethod
    def find_by_id(invoice_id: UUID, db: Session) -> ImportInvoice:
        return db.query(ImportInvoice).filter(ImportInvoice.id == invoice_id).first()

    @staticmethod
    def get_all(db: Session) -> List[ImportInvoice]:
        return db.query(ImportInvoice).all()
