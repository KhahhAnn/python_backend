from pydantic import BaseModel
from typing import List

class UserOut(BaseModel):
    email: str
    roles: List[str]
