from sqlalchemy import Column, Integer, String
from database import Base

class Size(Base):
    __tablename__ = 'sizes'

    id = Column(Integer, primary_key=True, autoincrement=True)  # ID tự động tăng
    name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Size(name={self.name}, quantity={self.quantity})>"
