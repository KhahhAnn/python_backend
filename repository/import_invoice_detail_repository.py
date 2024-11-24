from sqlalchemy.orm import Session
from uuid import UUID
from typing import List
from models.importInvoiceDetail import ImportInvoiceDetail

class ImportInvoiceDetailRepository:

    @staticmethod
    def add(self, db: Session, invoice_detail: ImportInvoiceDetail) -> ImportInvoiceDetail:
        db.add(invoice_detail)
        db.commit()
        db.refresh(invoice_detail)
        return invoice_detail

    @staticmethod
    def update(self, db: Session, invoice_detail: ImportInvoiceDetail) -> ImportInvoiceDetail:
        db.commit()
        db.refresh(invoice_detail)
        return invoice_detail

    @staticmethod
    def delete(self, db: Session, id: UUID):
        db.delete(id)
        db.commit()

    @staticmethod
    def get(self, db: Session, id: UUID) -> ImportInvoiceDetail:
        return db.query(ImportInvoiceDetail).filter(ImportInvoiceDetail.id == id).first()

    @staticmethod
    def save(import_invoice_detail: ImportInvoiceDetail, db: Session) -> ImportInvoiceDetail:
        db.add(import_invoice_detail)
        db.commit()
        db.refresh(import_invoice_detail)
        return import_invoice_detail

    @staticmethod
    def find_by_id(detail_id: UUID, db: Session) -> ImportInvoiceDetail:
        return db.query(ImportInvoiceDetail).filter(ImportInvoiceDetail.id == detail_id).first()

    @staticmethod
    def get_all(db: Session) -> List[ImportInvoiceDetail]:
        return db.query(ImportInvoiceDetail).all()
