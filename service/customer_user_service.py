from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from database import get_db
from models.user import Users
from repository.user_repository import UserRepository
from response.user_out import UserOut

class CustomerUserService:
    def __init__(self, user_repository: UserRepository = Depends(), db: Session = Depends(get_db)):
        self.user_repository = user_repository
        self.db = db
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def get_user_by_email(self, email: str) -> Users:
        user = self.user_repository.find_by_email(self.db, email)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    def authenticate_user(self, email: str, password: str) -> UserOut:
        user = self.get_user_by_email(email)
        if not self.pwd_context.verify(password, user.password):
            raise HTTPException(status_code=403, detail="Invalid credentials")

        roles = [role.role_name for role in user.roles_list]
        return UserOut(email=user.email, roles=roles)

    def get_user_roles(self, email: str) -> List[str]:
        user = self.get_user_by_email(email)
        return [role.role_name for role in user.roles_list]
