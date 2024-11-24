from pydantic import BaseModel

class ChangePasswordRequest(BaseModel):
    currentPassword: str
    password: str