from sqlalchemy.orm import Session
from uuid import UUID
from typing import List
from models.image import Images 

class ImageRepository:
    @staticmethod
    def save(image: Images, db: Session) -> Images:
        db.add(image)
        db.commit()
        db.refresh(image)
        return image

    @staticmethod
    def find_by_id(image_id: UUID, db: Session) -> Images:
        return db.query(Images).filter(Images.id == image_id).first()

    @staticmethod
    def get_all(db: Session) -> List[Images]:
        return db.query(Images).all()
