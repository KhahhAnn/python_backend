import jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

# Constants
SECRET_KEY = "S2hhbmhhbmJ1aTEwMTBAZ21haWwuY29tVHJhbmdibzIwMTIyMDAzQGdtYWlsLmNvbQ=="  # Replace with a secure key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 14100  # Equivalent to 846000000 ms in minutes

# Dependency for FastAPI security
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class JwtProvider:
    @staticmethod
    def generate_token(email: str) -> str:
        """Generates a JWT token."""
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode = {"email": email, "exp": expire}
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    @staticmethod
    def get_email_from_token(token: str) -> str:
        """Extracts email from a JWT token."""
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            email: str = payload.get("email")
            if email is None:
                raise HTTPException(status_code=403, detail="Token invalid")
            return email
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=403, detail="Token expired")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=403, detail="Token invalid")

# Dependency to get the current user
def get_current_user(token: str = Depends(oauth2_scheme)) -> str:
    """Retrieves the current user email from the JWT token."""
    email = JwtProvider.get_email_from_token(token)
    return email
