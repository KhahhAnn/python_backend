from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.orderItem import OrderItem
from service.order_item_service import OrderItemService
from repository.order_item_repository import OrderItemRepository
from database import get_db

router = APIRouter()

# Route để tạo một OrderItem mới
@router.post("/order-item", response_model=OrderItem)
def create_order_item(
    order_item: OrderItem,
    db: Session = Depends(get_db),
    service: OrderItemService = Depends(),
):
    try:
        return service.create_order_item(order_item)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
