from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schema.address_schema import AddressSchema
from database import get_db  # Giả sử bạn có hàm get_db để lấy session DB
from exception.user_exception import UserException
from service.address_service import AddressService
from service.user_service import UserService

router = APIRouter()

# Dependency to inject the AddressService
def get_address_service(db: Session) -> AddressService:
    user_service = UserService(db)
    return AddressService(user_service)

@router.get("/users/{user_id}/addresses", response_model=List[AddressSchema])
async def get_user_addresses(user_id: int, db: Session = Depends(get_db), address_service: AddressService = Depends(get_address_service)):
    try:
        # Lấy tất cả địa chỉ của người dùng
        addresses = address_service.get_all_addresses(user_id, db)
        return addresses
    except UserException as e:
        # Nếu người dùng không tồn tại
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        # Xử lý các lỗi khác
        raise HTTPException(status_code=500, detail=str(e))
