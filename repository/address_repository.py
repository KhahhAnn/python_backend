from sqlalchemy.orm import Session
from typing import List, Optional
from models.address import Address 

class AddressRepository:
    @staticmethod
    def get_all_addresses(db: Session) -> List[Address]:
        return db.query(Address).all()

    @staticmethod
    def get_address_by_id(address_id: int, db: Session) -> Optional[Address]:
        return db.query(Address).filter(Address.id == address_id).first()

    @staticmethod
    def create_address(address: Address, db: Session) -> Address:
        db.add(address)
        db.commit()
        db.refresh(address)
        return address

    @staticmethod
    def update_address(address: Address, db: Session) -> Address:
        db.merge(address)
        db.commit()
        return address

    @staticmethod
    def delete_address(address_id: int, db: Session):
        db.query(Address).filter(Address.id == address_id).delete()
        db.commit()
