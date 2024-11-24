from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.order import Order
from models.user import Users
from models.address import Address
from schema.order_schema import OrderSchema
from service.order_service import OrderService
from database import get_db
from response.api_response import ApiResponse

router = APIRouter()

# Route để tạo đơn hàng
@router.post("/order", response_model=OrderSchema)
def create_order(
    user: Users,
    shipping_address: Address,
    db: Session = Depends(get_db),
    service: OrderService = Depends(),
):
    try:
        return service.create_order(user, shipping_address)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Route để lấy thông tin đơn hàng theo ID
@router.get("/order/{order_id}", response_model=OrderSchema)
def get_order_by_id(order_id: int, db: Session = Depends(get_db), service: OrderService = Depends()):
    try:
        return service.find_order_by_id(order_id)
    except HTTPException as e:
        raise e

# Route để lấy lịch sử đơn hàng của người dùng
@router.get("/orders/{user_id}", response_model=List[OrderSchema])
def get_user_orders(user_id: int, db: Session = Depends(get_db), service: OrderService = Depends()):
    try:
        return service.user_order_history(user_id)
    except HTTPException as e:
        raise e

# Route để cập nhật đơn hàng
@router.put("/order/{order_id}", response_model=OrderSchema)
def update_order(
    order_id: int, order: Order, db: Session = Depends(get_db), service: OrderService = Depends()
):
    try:
        order.id = order_id  # Set order id for updating
        return service.update_order(order)
    except HTTPException as e:
        raise e

# Route để xóa đơn hàng
@router.delete("/order/{order_id}", response_model=ApiResponse)
def delete_order(order_id: int, db: Session = Depends(get_db), service: OrderService = Depends()):
    try:
        service.delete_order(order_id)
        return {"detail": "Order deleted successfully"}
    except HTTPException as e:
        raise e

# Route để lấy tất cả đơn hàng
@router.get("/orders", response_model=List[OrderResponse])
def get_all_orders(db: Session = Depends(get_db), service: OrderService = Depends()):
    try:
        return service.get_all_orders()
    except HTTPException as e:
        raise e
