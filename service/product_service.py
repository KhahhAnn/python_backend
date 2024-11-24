from datetime import date

from sqlalchemy.orm import Session

from models.category import Category
from models.product import Product
from repository.product_repository import ProductRepository


class ProductService:
    def __init__(self, db: Session):
        self.db = db
        self.repository = ProductRepository()

    def create_product(self, product_request: Product):
        # Create or get top-level category
        top_level = self.repository.get_category_by_name(self.db, product_request.top_level_category)
        if not top_level:
            top_level = Category(name=product_request.top_level_category, level=1)
            self.db.add(top_level)
            self.db.commit()

        # Create or get second-level category
        second_level = self.repository.get_category_by_name_and_parent(
            self.db, product_request.second_level_category, top_level.id
        )
        if not second_level:
            second_level = Category(name=product_request.second_level_category, parent_id=top_level.id, level=2)
            self.db.add(second_level)
            self.db.commit()

        # Create or get third-level category
        third_level = self.repository.get_category_by_name_and_parent(
            self.db, product_request.third_level_category, second_level.id
        )
        if not third_level:
            third_level = Category(name=product_request.third_level_category, parent_id=second_level.id, level=3)
            self.db.add(third_level)
            self.db.commit()

        product = Product(
            title=product_request.title,
            color=product_request.color,
            brand=product_request.brand,
            description=product_request.description,
            discounted_price=product_request.discounted_price,
            discount_percent=product_request.discount_percent,
            price=product_request.price,
            sizes=product_request.size,
            quantity=product_request.quantity,
            category_id=third_level.id,
            created_at=str(date.today()),  # Change as necessary
            image_url=product_request.image_url,
        )

        return self.repository.create_product(self.db, product)

    def delete_product(self, product_id: int):
        self.repository.delete_product(self.db, product_id)

    def update_product(self, product_id: int, req: Product):
        existing_product = self.repository.find_product_by_id(self.db, product_id)
        if not existing_product:
            raise Exception(f"Product not found with id - {product_id}")

        # Update fields as necessary
        if req.quantity is not None:
            existing_product.quantity = req.quantity

        return self.repository.update_product(self.db, existing_product)

    def find_product_by_id(self, product_id: int):
        product = self.repository.find_product_by_id(self.db, product_id)
        if not product:
            raise Exception(f"Product not found with id - {product_id}")
        return product

    def get_all_products(self):
        return self.repository.find_all_products(self.db)
