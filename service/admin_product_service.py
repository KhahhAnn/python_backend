from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends

from models.category import Category
from models.product import Product
from database import get_db
from request.add_product_request import AddProductRequest


class AdminProductService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def admin_update_product(self, product: Product) -> Product:
        exist_product = self.db.query(Product).filter(Product.id == product.id).first()
        if not exist_product:
            raise HTTPException(status_code=404, detail="Product not found")

        # Update fields
        exist_product.quantity = product.quantity
        exist_product.price = product.price
        exist_product.color = product.color
        exist_product.title = product.title
        exist_product.description = product.description
        exist_product.image_url = product.image_url
        exist_product.brand = product.brand
        exist_product.discounted_price = product.discounted_price

        self.db.commit()
        self.db.refresh(exist_product)
        return exist_product

    def admin_add_product(self, req: AddProductRequest) -> Product:
        category = self.db.query(Category).filter(Category.id == req.category_id).first()
        if not category:
            raise HTTPException(status_code=404, detail=f"Category not found for ID: {req.category_id}")

        # Create and save product
        product = Product(
            category=category,
            title=req.title,
            brand=req.brand,
            color=req.color,
            image_url=req.image_url,
            price=req.price,
            discounted_price=req.discounted_price,
            quantity=req.quantity
        )
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    def admin_delete_product(self, product_id: int):
        product = self.db.query(Product).filter(Product.id == product_id).first()
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        self.db.delete(product)
        self.db.commit()
