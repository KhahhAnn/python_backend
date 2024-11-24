from sqlalchemy.orm import Session
from service.user_service import UserService

from exception.user_exception import UserException
from models.address import Address


class AddressService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def get_all_addresses(self, user_id: int, db: Session) -> list[Address]:
        # Retrieve the user by ID using UserService
        user = self.user_service.find_user_by_id(user_id, db)

        # Check if the user exists
        if not user:
            raise UserException("User not found")

        # Return the list of addresses associated with the user
        return user.addresses  # Assuming `addresses` is the SQLAlchemy relationship name in the Users model
