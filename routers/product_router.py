from fastapi import APIRouter, HTTPException, Query, Depends
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models.product import Product
from schema.product_schema import ProductSchema
from service.product_service import ProductService

router = APIRouter()

@router.get("/products", response_model=List[ProductSchema])
async def get_products(
    category: str,
    color: List[str] = Query(...),
    size: List[str] = Query(...),
    minPrice: int = Query(...),
    maxPrice: int = Query(...),
    minDiscount: int = Query(...),
    sort: str = Query(...),
    stock: str = Query(...),
    pageNumber: int = Query(...),
    pageSize: int = Query(...),
    db: Session = Depends(get_db)
):
    product_service = ProductService(db)
    try:
        products = product_service.get_all_product(category, color, size, minPrice, maxPrice, minDiscount, sort, stock, pageNumber, pageSize)
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/products/{product_id}", response_model=ProductSchema)
async def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    product_service = ProductService(db)
    try:
        product = product_service.find_product_by_id(product_id)
        return product
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/products", response_model=ProductSchema)
async def create_product(product_request: ProductSchema, db: Session = Depends(get_db)):
    product_service = ProductService(db)
    try:
        new_product = product_service.create_product(product_request)
        return new_product
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/products/{product_id}", response_model=ProductSchema)
async def update_product(product_id: int, product_request: ProductSchema, db: Session = Depends(get_db)):
    product_service = ProductService(db)
    try:
        updated_product = product_service.update_product(product_id, product_request)
        return updated_product
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Product not found with id - {product_id}: {str(e)}")

@router.delete("/products/{product_id}", status_code=204)
async def delete_product(product_id: int, db: Session = Depends(get_db)):
    product_service = ProductService(db)
    try:
        product_service.delete_product(product_id)
        return {"message": "Product deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Product not found with id - {product_id}: {str(e)}")
