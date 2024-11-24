from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models.product import Product
from service.admin_product_service import AdminProductService
from request.add_product_request import AddProductRequest
from database import get_db

router = APIRouter()

def get_admin_product_service(db: Session = Depends(get_db)) -> AdminProductService:
    return AdminProductService(db)

@router.post("/products")
async def add_product(req: AddProductRequest, db: Session = Depends(get_db), product_service: AdminProductService = Depends(get_admin_product_service)):
    try:
        product = product_service.admin_add_product(req)
        return {"message": "Product added successfully", "product": product}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.put("/products/{product_id}")
async def update_product(product_id: int, product: Product, db: Session = Depends(get_db), product_service: AdminProductService = Depends(get_admin_product_service)):
    try:
        product.id = product_id  # Ensure the product ID is set for the update
        updated_product = product_service.admin_update_product(product)
        return {"message": "Product updated successfully", "product": updated_product}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.delete("/products/{product_id}")
async def delete_product(product_id: int, db: Session = Depends(get_db), product_service: AdminProductService = Depends(get_admin_product_service)):
    try:
        product_service.admin_delete_product(product_id)
        return {"message": "Product deleted successfully"}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
