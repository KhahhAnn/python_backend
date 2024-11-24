from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from service.customer_user_service import CustomerUserService
from request.login_request import LoginRequest
from response.user_out import UserOut
from database import get_db

router = APIRouter()

# Đăng nhập người dùng và trả về các thông tin cần thiết (ví dụ: email và roles)
@router.post("/login", response_model=UserOut)
def login(
    req: LoginRequest,
    user_service: CustomerUserService = Depends(),
    db: Session = Depends(get_db),
):
    return user_service.authenticate_user(req.email, req.password)

# Lấy thông tin người dùng theo email
@router.get("/user/{email}", response_model=UserOut)
def get_user_by_email(
    email: str,
    user_service: CustomerUserService = Depends(),
    db: Session = Depends(get_db),
):
    user = user_service.get_user_by_email(email)
    return UserOut(email=user.email, roles=[role.role_name for role in user.roles_list])

# Lấy danh sách các roles của người dùng
@router.get("/user/{email}/roles", response_model=List[str])
def get_user_roles(
    email: str,
    user_service: CustomerUserService = Depends(),
    db: Session = Depends(get_db),
):
    return user_service.get_user_roles(email)
