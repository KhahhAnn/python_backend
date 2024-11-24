import uuid
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from passlib.context import CryptContext
from email_service import EmailService
from models.roles import Role
from models.user import Users


class AccountService:
    def __init__(self, email_service: EmailService):
        self.email_service = email_service
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash_password(self, password: str) -> str:
        return self.pwd_context.hash(password)

    def create_active_code(self) -> str:
        return str(uuid.uuid4())

    def register(self, user_data, db: Session):
        # Check if the email is already registered
        if db.query(Users).filter(Users.email == user_data.email).first():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email exists")

        # Ensure a password is provided
        if not user_data.password:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Password cannot be null")

        # Hash password and create user
        hashed_password = self.hash_password(user_data.password)
        active_code = self.create_active_code()
        new_user = Users(
            email=user_data.email,
            password=hashed_password,
            active_code=active_code,
            is_active=False
        )

        # Assign default role
        default_role = db.  query(Role).filter(Role.role_name == "ROLE_USER").first()
        if default_role:
            new_user.roles.append(default_role)

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        # Send activation email
        self.send_mail_active_code(new_user.email, new_user.active_code)
        return "Register success!"

    def send_mail_active_code(self, email: str, active_code: str):
        subject = "Activate your account at Aniestore"
        body = f"""<html><body>
        <p>Please use the following code to activate your account: <strong>{active_code}</strong></p>
        <p>Or click the link to activate: <a href='http://localhost:8000/auth/activate/{email}/{active_code}'>Activate Account</a></p>
        </body></html>"""
        self.email_service.send_email("noreply@aniestore.com", email, subject, body)

    def activate_account(self, email: str, active_code: str, db: Session):
        user = db.query(Users).filter(Users.email == email).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Account not exist")

        if user.is_active:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Account has already been activated")

        if user.active_code == active_code:
            user.is_active = True
            user.active_code = None
            db.commit()
            return "Account activated successfully"
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid activation code")
