from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from service.account_service import AccountService
from database import get_db  # Giả sử bạn có hàm get_db để lấy session DB
from service.email_service import EmailService

router = APIRouter()

# Pydantic models for request validation
class UserRegisterRequest(BaseModel):
    email: str
    password: str


class AccountActivateRequest(BaseModel):
    email: str
    active_code: str


# Dependency to inject AccountService
def get_account_service(db: Session) -> AccountService:
    email_service = EmailService()
    return AccountService(email_service)


@router.post("/register")
async def register(user_data: UserRegisterRequest, db: Session = Depends(get_db), account_service: AccountService = Depends(get_account_service)):
    try:
        return {"message": account_service.register(user_data, db)}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.post("/activate")
async def activate_account(account_data: AccountActivateRequest, db: Session = Depends(get_db), account_service: AccountService = Depends(get_account_service)):
    try:
        return {"message": account_service.activate_account(account_data.email, account_data.active_code, db)}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

