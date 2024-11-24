from pydantic import BaseModel
from typing import List

class AuthResponse(BaseModel):
    jwt: str
    message: str
    permission: List[str]