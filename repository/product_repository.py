from sqlalchemy.orm import Session
from sqlalchemy import asc, desc, or_
from typing import List, Optional

from models.category import Category
from models.product import Product

class ProductRepository:
    @staticmethod
    def filter_products(
        category: str,
        min_price: Optional[int],
        max_price: Optional[int],
        min_discount: Optional[int],
        sort: Optional[str],
        db: Session
    ) -> List[Product]:

        query = db.query(Product)

        # Category filter
        if category:
            query = query.filter(Product.category.has(name=category))

        # Price range filter
        if min_price is not None and max_price is not None:
            query = query.filter(Product.discounted_price.between(min_price, max_price))

        # Minimum discount filter
        if min_discount is not None:
            query = query.filter(Product.discount_percent >= min_discount)

        # Sorting
        if sort == 'price_low':
            query = query.order_by(asc(Product.discounted_price))
        elif sort == 'price_high':
            query = query.order_by(desc(Product.discounted_price))

        return query.all()

    @staticmethod
    def save(product: Product, db: Session) -> Product:
        db.add(product)
        db.commit()
        db.refresh(product)
        return product

    @staticmethod
    def find_by_id(product_id: int, db: Session) -> Optional[Product]:
        return db.query(Product).filter(Product.id == product_id).first()

    def create_product(self, db: Session, product: Product):
        db.add(product)
        db.commit()
        db.refresh(product)
        return product

    def delete_product(self, db: Session, product_id: int):
        product = db.query(Product).filter(Product.id == product_id).first()
        if product:
            db.delete(product)
            db.commit()

    def update_product(self, db: Session, product: Product):
        db.commit()
        db.refresh(product)
        return product

    def find_product_by_id(self, db: Session, product_id: int):
        return db.query(Product).filter(Product.id == product_id).first()

    def find_all_products(self, db: Session):
        return db.query(Product).all()

    def get_category_by_name_and_parent(self, db: Session, category_name: str, parent_id: int):
        return db.query(Category).filter(Category.name == category_name, Category.parent_id == parent_id).first()

    def get_category_by_name(self, db: Session, category_name: str):
        return db.query(Category).filter(Category.name == category_name).first()