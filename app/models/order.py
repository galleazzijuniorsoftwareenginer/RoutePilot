from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.database import Base


class Order(Base):

    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)

    customer_name = Column(String, nullable=False)
    address = Column(String)

    latitude = Column(Float)
    longitude = Column(Float)

    status = Column(String, default="pending")

    company_id = Column(Integer, ForeignKey("companies.id"))
