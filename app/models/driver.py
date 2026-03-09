from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base


class Driver(Base):

    __tablename__ = "drivers"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)
    phone = Column(String)

    company_id = Column(Integer, ForeignKey("companies.id"))
