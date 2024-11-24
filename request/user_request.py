from pydantic import BaseModel
from typing import Optional

from models.user import Users


class UserRequest(BaseModel):
    user: Users
    img: Optional[str] = None