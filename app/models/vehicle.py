from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base


class Vehicle(Base):

    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)

    plate = Column(String, nullable=False)
    capacity = Column(Integer)

    company_id = Column(Integer, ForeignKey("companies.id"))
