from sqlalchemy.orm import Session
from typing import List
from models.roles import Role


class RoleRepository:
    @staticmethod
    def find_by_role_name(role_name: str, db: Session) -> List[Role]:
        return db.query(Role).filter(Role.role_name == role_name).all()

    @staticmethod
    def save(role: Role, db: Session) -> Role:
        db.add(role)
        db.commit()
        db.refresh(role)
        return role

    @staticmethod
    def find_by_id(role_id: str, db: Session) -> Role:
        return db.query(Role).filter(Role.id == role_id).first()
