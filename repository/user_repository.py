from sqlalchemy.orm import Session

from models.user import Users


class UserRepository:
    @staticmethod
    def find_by_email(email: str, db: Session) -> Users:
        return db.query(Users).filter(Users.email == email).first()

    @staticmethod
    def find_by_email_and_password(email: str, password: str, db: Session) -> Users:
        return db.query(Users).filter(Users.email == email, Users.password == password).first()

    @staticmethod
    def exists_by_email(email: str, db: Session) -> bool:
        return db.query(Users).filter(Users.email == email).first() is not None

    @staticmethod
    def save(user: Users, db: Session) -> Users:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def find_by_id(user_id: int, db: Session) -> Users:
        return db.query(Users).filter(Users.id == user_id).first()
