from sqlalchemy.orm import Session
from uuid import UUID
from typing import List
from models.event import Event

class EventRepository:
    @staticmethod
    def save(event: Event, db: Session) -> Event:
        db.add(event)
        db.commit()
        db.refresh(event)
        return event

    @staticmethod
    def find_by_id(event_id: UUID, db: Session) -> Event:
        return db.query(Event).filter(Event.id == event_id).first()

    @staticmethod
    def get_all(db: Session) -> List[Event]:
        return db.query(Event).all()
