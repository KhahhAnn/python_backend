from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi import HTTPException, Depends
from config.jwt_provider import JwtProvider
from database import get_db
from models.user import Users
from request.change_password_request import ChangePasswordRequest
from request.user_request import UserRequest
from response.api_response import ApiResponse

# Password context for hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    def __init__(self, db: Session, jwt_provider: JwtProvider):
        self.db = db
        self.jwt_provider = jwt_provider

    def find_user_by_id(self, user_id: int) -> Users:
        user = self.db.query(Users).filter(Users.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail=f"User not found with id - {user_id}")
        return user

    def find_user_profile_by_jwt(self, jwt: str) -> Users:
        email = self.jwt_provider.get_email_from_token(jwt)
        user = self.db.query(Users).filter(Users.email == email).first()
        if not user:
            raise HTTPException(status_code=404, detail=f"User not found with email - {email}")
        return user

    def update_user(self, jwt: str, user_request: UserRequest) -> Users:
        user = self.find_user_profile_by_jwt(jwt)
        user.first_name = user_request.first_name
        user.last_name = user_request.last_name
        user.email = user_request.email
        user.image_src = user_request.image_src
        self.db.commit()
        self.db.refresh(user)  # To get the updated object
        return user

    def change_password(self, jwt: str, change_password_request: ChangePasswordRequest) -> Users:
        user = self.find_user_profile_by_jwt(jwt)
        if not pwd_context.verify(change_password_request.current_password, user.password):
            raise HTTPException(status_code=400, detail="Incorrect current password")
        user.password = pwd_context.hash(change_password_request.new_password)
        self.db.commit()
        self.db.refresh(user)  # To get the updated object
        return user

    def add_new_user(self, user: Users) -> ApiResponse:
        existing_user = self.db.query(Users).filter(Users.email == user.email).first()
        if existing_user:
            return ApiResponse(message="Email is already registered!", status=False)
        user.password = pwd_context.hash(user.password)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)  # To get the saved object
        return ApiResponse(message="User account saved successfully!", status=True)

    def update_user_info(self, user: Users) -> Users:
        existing_user = self.db.query(Users).filter(Users.email == user.email).first()
        if not existing_user:
            raise HTTPException(status_code=404, detail="User not found")
        existing_user.first_name = user.first_name
        existing_user.last_name = user.last_name
        existing_user.image_src = user.image_src
        existing_user.password = pwd_context.hash(user.password)
        self.db.commit()
        self.db.refresh(existing_user)  # To get the updated object
        return existing_user
