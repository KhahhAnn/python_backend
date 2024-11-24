from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models.user import Users
from request.add_item_request import AddItemRequest
from response.cart_response import CartResponse
from service.cart_service import CartService
from repository.user_repository import UserRepository

router = APIRouter()

# Khởi tạo CartService
@router.post("/cart/{user_id}/items", response_model=str)
def add_item_to_cart(
    user_id: int,
    req: AddItemRequest,
    cart_service: CartService = Depends(),
    db: Session = Depends(get_db),
):
    # Gọi phương thức add_cart_item từ CartService
    return cart_service.add_cart_item(user_id, req)

@router.get("/cart/{user_id}", response_model=CartResponse)
def get_user_cart(
    user_id: int,
    page: int = 1,
    page_size: int = 10,
    cart_service: CartService = Depends(),
    db: Session = Depends(get_db),
):
    # Gọi phương thức find_user_cart từ CartService để lấy giỏ hàng của người dùng
    return cart_service.find_user_cart(user_id, page, page_size)

@router.delete("/cart/{user_id}/items/{cart_item_id}", response_model=str)
def remove_item_from_cart(
    user_id: int,
    cart_item_id: int,
    cart_service: CartService = Depends(),
    db: Session = Depends(get_db),
):
    # Gọi phương thức remove_cart_item từ CartService để xóa sản phẩm khỏi giỏ
    return cart_service.remove_cart_item(user_id, cart_item_id)

@router.put("/cart/{user_id}/items/{cart_item_id}", response_model=str)
def update_cart_item(
    user_id: int,
    cart_item_id: int,
    req: AddItemRequest,
    cart_service: CartService = Depends(),
    db: Session = Depends(get_db),
):
    # Gọi phương thức update_cart_item từ CartService để cập nhật sản phẩm trong giỏ
    return cart_service.update_cart_item(user_id, cart_item_id, req)

@router.get("/cart/{user_id}/count", response_model=int)
def count_cart_items(
    user_id: int,
    cart_service: CartService = Depends(),
    db: Session = Depends(get_db),
):
    # Gọi phương thức count_cart_items từ CartService để đếm số sản phẩm trong giỏ
    return cart_service.count_cart_items(user_id)

@router.delete("/cart/{user_id}/clear", response_model=str)
def clear_cart(
    user_id: int,
    cart_service: CartService = Depends(),
    db: Session = Depends(get_db),
):
    # Gọi phương thức clear_cart từ CartService để xóa tất cả sản phẩm trong giỏ
    return cart_service.clear_cart(user_id)

@router.post("/cart/{user_id}/checkout", response_model=str)
def checkout_cart(
    user_id: int,
    cart_service: CartService = Depends(),
    db: Session = Depends(get_db),
):
    # Gọi phương thức checkout từ CartService để thực hiện thanh toán và xóa giỏ hàng
    return cart_service.checkout(user_id)
