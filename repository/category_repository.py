from sqlalchemy.orm import Session
from sqlalchemy import select
from uuid import UUID
from typing import Optional
from models.category import Category

class CategoryRepository:
    @staticmethod
    def get_reference_by_id(category_id: int, db: Session) -> Optional[Category]:
        return db.query(Category).filter(Category.id == category_id).first()
    @staticmethod
    def find_by_name(name: str, db: Session) -> Optional[Category]:
        return db.query(Category).filter(Category.name == name).first()

    @staticmethod
    def find_by_name_and_parent(name: str, parent_category_name: str, db: Session) -> Optional[Category]:
        return db.query(Category).filter(
            Category.name == name,
            Category.parent_category.has(name=parent_category_name)
        ).first()
